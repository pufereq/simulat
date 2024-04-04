# -*- coding: utf-8 -*-
"""Game map module for GameScene."""

from __future__ import annotations

import logging as lg
from typing import Final

import pygame as pg

from src.simulat.core.characters.player import Player
from src.simulat.core.game import simulat
from src.simulat.core.characters.camera import Camera
from src.simulat.core.surfaces.game_map.tiles.tile import Tile, tiles_to_px
from src.simulat.core.surfaces.surface import Surface
from src.simulat.data.map_layout import MapLayout


class GameMap(Surface):
    """Game map class.

    The game map is the surface where the game takes place. It is a grid of
    tiles (see `Tile` class) that can be walls, floors, doors, etc. The game
    map is a subsurface of the game scene.
    """
    def __init__(self, scene: Scene) -> None:
        """Initialize the game map."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.debug("Initializing game map surface...")

        self.scene = scene

        # self.MAP_SIZE: Final = (80, 80)  # tiles
        self.MAP_SIZE: Final = (len(MapLayout.get_map_layout()[0]),
                                len(MapLayout.get_map_layout()))

        self.surface_size = (
            tiles_to_px(self.MAP_SIZE[0]),
            tiles_to_px(self.MAP_SIZE[1])
        )

        self.display_size: tuple = (
            scene.size[0] - scene.sidebar.SIDEBAR_SIZE[0],
            scene.size[1]
        )

        self.player = Player(self, (9, 9))
        self.character_surface = Surface(self.surface_size)
        self.character_surface.surface.set_colorkey((0, 0, 0))

        self.camera = Camera(self, self.player.pos)

        self.logger.debug(f"Game map size: {self.MAP_SIZE} tiles, "
                          f"{self.surface_size} px")

        # initialize surface
        super().__init__(self.surface_size)
        simulat.focused_surfaces[self] = True

        # initialize tiles
        self.tile_surface = Surface(self.surface_size)
        self._init_tiles()

    def input(self, *, events: list[pg.event.Event], keys: dict[int, bool]) -> None:
        """Handle input events.

        Args:
            key: The keys pressed.
        """

        camera_attached: bool = False

        # camera movement
        if keys[pg.K_UP]:
            self.camera.velocity[1] += -1
        if keys[pg.K_DOWN]:
            self.camera.velocity[1] += 1
        if keys[pg.K_LEFT]:
            self.camera.velocity[0] += -1
        if keys[pg.K_RIGHT]:
            self.camera.velocity[0] += 1

        # player movement
        if keys[pg.K_w]:
            self.player.velocity[1] += -1
            camera_attached = True
        if keys[pg.K_s]:
            self.player.velocity[1] += 1
            camera_attached = True
        if keys[pg.K_a]:
            self.player.velocity[0] += -1
            camera_attached = True
        if keys[pg.K_d]:
            self.player.velocity[0] += 1
            camera_attached = True

        if camera_attached:
            self.camera.pos = self.player.pos

    def update(self, delta: float) -> None:
        """Update the game map."""
        self.player.update(delta)
        self.camera.update(delta)

    def render(self) -> None:
        """Render the game map."""
        # Calculate the distance the player can move in one frame.
        # We only want to fill the area the player has moved out of, not the
        # whole map.
        player_step_x = self.player.max_speed * simulat.frame_delta + self.player.rect.width
        player_step_y = self.player.max_speed * simulat.frame_delta + self.player.rect.height

        # Fill the area the player has moved out of with black (color key).
        self.character_surface.surface.fill(
            (0, 0, 0),
            (
                self.player.rect.left - player_step_x,
                self.player.rect.top - player_step_y,
                self.player.rect.right + player_step_x,
                self.player.rect.bottom + player_step_y
            )
        )

        # Render the visible parts of the tile surface onto the main
        # (game_map) surface.
        self.blit(
            self.tile_surface.surface,
            (0, 0),
            self.camera.rect
        )

        # Render the player onto the character surface.
        self.player.render()

        # Render the visible parts of character surface onto the main
        # (game_map) surface.
        self.blit(
            self.character_surface.surface,
            (0, 0),
            self.camera.rect
        )

        # draw onto the game scene
        self.scene.surface.blit(self.surface, (0, 0))

    def _init_tiles(self):
        """Initialize the map tiles."""
        self.tiles = []
        self.collider_tiles = []

        for y, row in enumerate(MapLayout.get_map_layout()):
            self.tiles.append([])
            for x, char in enumerate(row):
                self.tiles[y].append(
                    MapLayout.get_tile_from_char(char)(self, (x, y))
                )
                self.tiles[y][x].draw()
                if self.tiles[y][x].is_collider:
                    self.collider_tiles.append(self.tiles[y][x])
