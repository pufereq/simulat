# -*- coding: utf-8 -*-
"""Game map module for GameScene."""

from __future__ import annotations
from typing import Final

import logging as lg
import pygame as pg

from ....game import simulat

from ...surface import Surface
from ....time_it import time_it

from .tile import Tile, tiles_to_px


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

        self.MAP_SIZE: Final = (40, 40)  # tiles

        self.surface_size = (
            tiles_to_px(self.MAP_SIZE[0]),
            tiles_to_px(self.MAP_SIZE[1])
        )

        self.camera = pg.Rect((0, 0), self.surface_size)

        self.logger.debug(f"Game map size: {self.MAP_SIZE} tiles, "
                          f"{self.surface_size} px")

        # initialize surface
        super().__init__(self.surface_size)
        simulat.focused_surfaces[self] = True

        # initialize tiles
        self._init_tiles()

    def input(self, key: pg.key) -> None:
        """Handle input events."""
        if key[pg.K_UP]:
            self.camera.y -= tiles_to_px(0.5)
        if key[pg.K_DOWN]:
            self.camera.y += tiles_to_px(0.5)
        if key[pg.K_LEFT]:
            self.camera.x -= tiles_to_px(0.5)
        if key[pg.K_RIGHT]:
            self.camera.x += tiles_to_px(0.5)

        self._update_camera_pos()

    def update(self) -> None:
        self._update_camera_pos()

    def _update_camera_pos(self) -> None:
        """Update the camera position."""
        self.camera.x = min(max(self.camera.x, 0),
                            self.surface_size[0] - simulat.SIZE[0])
        self.camera.y = min(max(self.camera.y, 0),
                            self.surface_size[1] - simulat.SIZE[1])

    @time_it
    def _init_tiles(self):
        """Initialize the map tiles."""
        self.tiles = []
        for y in range(self.MAP_SIZE[1]):
            self.tiles.append([])
            for x in range(self.MAP_SIZE[0]):
                self.tiles[y].append(Tile(self, (x, y)))
