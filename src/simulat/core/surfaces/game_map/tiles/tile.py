# -*- coding: utf-8 -*-
"""Tile module for GameMap."""

from __future__ import annotations

import logging as lg
from typing import Final

from src.simulat.core.surfaces.surface import Surface


TILE_SIZE: Final = 64  # pixels


class Tile():
    """Tile base class.

    A tile is a square on the game map. It can be a wall, a floor, a door, etc.
    Each tile type has its own class, which inherits from this class.
    """
    _id = 0

    def __init__(self, game_map: GameMap, pos: tuple[int, int]) -> None:
        """Initialize the tile."""
        Tile._id += 1

        self.id = Tile._id
        self.name = "Tile"

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

        self.surface = Surface((self.size, self.size), self.px_pos)

        self.rect = self.surface.surface.get_rect(topleft=self.px_pos)

        self.is_collider = False

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
        self.game_map.tile_surface.blit(self.surface.surface, self.surface.pos)


def tiles_to_px(tiles: int | float) -> int:
    """Convert tiles to pixels."""
    return round(tiles * TILE_SIZE)


def px_to_tiles(px: int) -> float:
    """Convert pixels to tiles."""
    return px / TILE_SIZE
