# -*- coding: utf-8 -*-
"""Game map module for GameScene."""

from __future__ import annotations

import logging as lg
from typing import Final

import pygame as pg

from src.simulat.data.colors import BasicPalette
from src.simulat.core.characters.player import Player
from src.simulat.core.game import simulat
from src.simulat.core.characters.camera import Camera
from src.simulat.core.surfaces.game_map.tiles.tile import TILE_SIZE, Tile, tiles_to_px
from src.simulat.core.surfaces.surface import Surface
from src.simulat.core.time_it import time_it
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

        self.hovered_overlay: Surface = Surface(self.surface_size)
        self.hovered_overlay.surface.set_colorkey(BasicPalette.MAGENTA)
        self.hovered_overlay.surface.fill(BasicPalette.MAGENTA)

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

    def input(self, key: ScancodeWrapper) -> None:
        """Handle input events.

        Args:
            key: The keys pressed.
        """

        camera_attached: bool = False

        # camera movement
        if key[pg.K_UP]:
            self.camera.velocity[1] += -1
        if key[pg.K_DOWN]:
            self.camera.velocity[1] += 1
        if key[pg.K_LEFT]:
            self.camera.velocity[0] += -1
        if key[pg.K_RIGHT]:
            self.camera.velocity[0] += 1

        # player movement
        if key[pg.K_w]:
            self.player.velocity[1] += -1
            camera_attached = True
        if key[pg.K_s]:
            self.player.velocity[1] += 1
            camera_attached = True
        if key[pg.K_a]:
            self.player.velocity[0] += -1
            camera_attached = True
        if key[pg.K_d]:
            self.player.velocity[0] += 1
            camera_attached = True

        if camera_attached:
            self.camera.pos = self.player.pos

    def update(self, delta: float) -> None:
        """Update the game map."""
        # get the mouse position and display the tile the mouse is over
        mouse_pos = pg.mouse.get_pos()

        # translate the mouse position to the game map
        tile_pos = (
            mouse_pos[0] + self.camera.rect.left,
            mouse_pos[1] + self.camera.rect.top
        )

        # get the tile the mouse is over
        self.hovered_tile = self.tiles[tile_pos[1] // TILE_SIZE][tile_pos[0] // TILE_SIZE]
        # self.logger.debug(f"Mouse over tile: {self.hovered_tile}")
        simulat.topbar.update_details(f"{self.hovered_tile}")

        self.player.update(delta)
        self.camera.update(delta)

    def render(self) -> None:
        """Render the game map."""
        # Calculate the distance the player can move in one frame.
        # We only want to fill the area the player has moved out of, not the
        # whole map.
        player_step_x = self.player.max_speed * simulat.frame_delta + self.player.rect.width
        player_step_y = self.player.max_speed * simulat.frame_delta + self.player.rect.height

        # render the tile onto the tile surface
        # if self.prev_tile:
        #     self.prev_tile.draw()
        # self.logger.debug(f"Hovered tile: {self.hovered_tile.hovered}")
        # self.hovered_tile.draw()

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

        # Render the visible parts of the hovered overlay surface onto the main
        # (game_map) surface.
        self.hovered_overlay.surface.fill(
            BasicPalette.MAGENTA,
            self.camera.rect
        )
        # show red overlay on the tile the mouse is over
        tile_color = self.hovered_tile.surface.surface.get_at((0, 0))
        # make tile_color negative
        tile_color = tuple([255 - c for c in tile_color])
        pg.draw.rect(
            self.hovered_overlay.surface,
            tile_color,
            (
                self.hovered_tile.px_pos[0],
                self.hovered_tile.px_pos[1],
                TILE_SIZE,
                TILE_SIZE
            ),
            1
        )

        self.blit(
            self.hovered_overlay.surface,
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

    @time_it
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
