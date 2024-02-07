# -*- coding: utf-8 -*-
"""Game map module for GameScene."""

from __future__ import annotations

import logging as lg
from typing import Final

import pygame as pg
from src.simulat.core.characters.player import Player

from src.simulat.core.game import simulat
from src.simulat.core.surfaces.game_map.camera import Camera
from src.simulat.core.surfaces.game_map.tiles.tile import Tile, tiles_to_px
from src.simulat.core.surfaces.surface import Surface
from src.simulat.core.time_it import time_it


class GameMap(Surface):
    """Game map class.

    The game map is the surface where the game takes place. It is a grid of
    tiles (see `Tile` class) that can be walls, floors, doors, etc. The game
    map is a subsurface of the game scene.
    """
    def __init__(self) -> None:
        """Initialize the game map."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.debug("Initializing game map surface...")

        self.MAP_SIZE: Final = (80, 80)  # tiles

        self.surface_size = (
            tiles_to_px(self.MAP_SIZE[0]),
            tiles_to_px(self.MAP_SIZE[1])
        )

        self.player = Player(self, (9, 9))

        self.camera = Camera(self)

        self.logger.debug(f"Game map size: {self.MAP_SIZE} tiles, "
                          f"{self.surface_size} px")

        # initialize surface
        super().__init__(self.surface_size)
        simulat.focused_surfaces[self] = True

        # initialize tiles
        self.tile_surface = Surface(self.surface_size)
        self._init_tiles()

    def input(self, key: ScancodeWrapper) -> None:
        """Handle input events."""
        if key[pg.K_UP]:
            self.player.velocity[1] += -1
        if key[pg.K_DOWN]:
            self.player.velocity[1] += 1
        if key[pg.K_LEFT]:
            self.player.velocity[0] += -1
        if key[pg.K_RIGHT]:
            self.player.velocity[0] += 1

    def update(self) -> None:
        self.camera.update()
        self.player.update()

    def render(self) -> None:
        """Render the game map."""
        self.blit(
            self.tile_surface.surface,
            (0, 0),
        )
        self.player.render()

    @time_it
    def _init_tiles(self):
        """Initialize the map tiles."""
        self.tiles = []
        for y in range(self.MAP_SIZE[1]):
            self.tiles.append([])
            for x in range(self.MAP_SIZE[0]):
                self.tiles[y].append(Tile(self, (x, y)))
                self.tiles[y][x].draw()
