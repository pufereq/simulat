# -*- coding: utf-8 -*-
"""Collider tile baseclass module."""

from __future__ import annotations

from src.simulat.core.surfaces.game_map.tiles.tile import Tile


class ColliderTile(Tile):
    """Collider tile class.

    A collider tile is a tile that cannot be walked through. It inherits from
    `Tile`.
    """

    def __init__(self, game_map: GameMap, pos: tuple[int, int]) -> None:
        """Initialize the collider tile."""
        super().__init__(game_map, pos)

        self.is_collider = True

    def __repr__(self) -> str:
        """Return a string representation of the collider tile."""
        return f"{type(self).__name__}({self.pos})"

    def __str__(self) -> str:
        """Return a user-friendly representation of the collider tile."""
        return f"{type(self).__name__} at {self.pos}"

    def draw(self) -> None:
        """Draw the collider tile."""
        self.surface.fill((255, 0, 0))
        super().draw()
