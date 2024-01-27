# -*- coding: utf-8 -*-
"""Tile module for GameMap."""

from __future__ import annotations

import logging as lg
from typing import Final


TILE_SIZE: Final = 64  # pixels


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
            self.pos_x * TILE_SIZE,
            self.pos_y * TILE_SIZE
        )

        self.size = TILE_SIZE
        self.width = self.size
        self.height = self.size

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.surface = self.game_map.subsurface(self.px_pos,
                                                (self.size, self.size))

        # NOTE: this is just a placeholder, it will be replaced by the actual
        # tile image/character depending on the tile type.
        self.surface.fill((self.pos_x * 16 % 255, self.pos_y * 16 % 255,
                           (self.pos_x + self.pos_y) * 8 % 255))

    def __repr__(self) -> str:
        """Return a string representation of the tile."""
        return f"{type(self).__name__}({self.pos})"

    def __str__(self) -> str:
        """Return a user-friendly representation of the tile."""
        return f"{type(self).__name__} at {self.pos}"

    def draw(self):
        """Draw the tile. NOTE: this method is not used. The tiles are drawn
        directly on the game map. (see
        https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface).
        """
        self.game_map.blit(self.surface.surface, self.surface.pos)


def tiles_to_px(tiles: int | float) -> int:
    """Convert tiles to pixels."""
    return round(tiles * TILE_SIZE)


def px_to_tiles(px: int) -> int:
    """Convert pixels to tiles."""
    if px % TILE_SIZE != 0:
        raise ValueError(f"px ({px}) is not a multiple of TILE_SIZE "
                         f"({TILE_SIZE})")
    return px // TILE_SIZE
