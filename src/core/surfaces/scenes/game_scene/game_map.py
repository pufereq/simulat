# -*- coding: utf-8 -*-
"""Game map module for GameScene."""

from __future__ import annotations
from typing import Final

import logging as lg

from ...surface import Surface
from ....time_it import time_it

from .tile import Tile


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

        self.TILE_SIZE: Final = 32  # pixels
        self.MAP_SIZE: Final = (40, 40)  # tiles

        self.surface_size = (
            self.TILE_SIZE * self.MAP_SIZE[0],
            self.TILE_SIZE * self.MAP_SIZE[1]
        )

        self.logger.debug(f"Game map size: {self.MAP_SIZE} tiles, "
                          f"{self.surface_size} px")

        # initialize surface
        super().__init__(self.surface_size)

        # initialize tiles
        self._init_tiles()

    @time_it
    def _init_tiles(self):
        """Initialize the map tiles."""
        self.tiles = []
        for y in range(self.MAP_SIZE[1]):
            self.tiles.append([])
            for x in range(self.MAP_SIZE[0]):
                self.tiles[y].append(Tile(self, (x, y)))
