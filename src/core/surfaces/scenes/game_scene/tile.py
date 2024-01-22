# -*- coding: utf-8 -*-
"""Tile module for GameMap."""

from __future__ import annotations

import logging as lg


class Tile():
    """Tile base class.

    A tile is a square on the game map. It can be a wall, a floor, a door, etc.
    Each tile type has its own class, which inherits from this class.
    """
    def __init__(self, game_map: GameMap, pos: tuple[int, int]) -> None:
        """Initialize the tile."""
        self.game_map = game_map
        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.px_pos = (
            self.pos_x * self.game_map.TILE_SIZE,
            self.pos_y * self.game_map.TILE_SIZE
        )

        self.size = self.game_map.TILE_SIZE
        self.width = self.size
        self.height = self.size

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.surface = self.game_map.subsurface(self.px_pos,
                                                (self.size, self.size))

        # NOTE: this is just a placeholder, it will be replaced by the actual
        # tile image/character depending on the tile type.
        self.surface.fill((self.pos_x * 16 % 255, self.pos_y * 16 % 255,
                           (self.pos_x + self.pos_y) * 8 % 255))

    def draw(self):
        """Draw the tile."""
        self.game_map.blit(self.surface.surface, self.surface.pos)