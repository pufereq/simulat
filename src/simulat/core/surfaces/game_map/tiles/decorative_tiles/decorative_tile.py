# -*- coding: utf-8 -*-
"""Decorative tile baseclass module."""

from __future__ import annotations

from src.simulat.core.surfaces.game_map.tiles.tile import Tile


class DecorativeTile(Tile):
    """Decorative tile class.

    A decorative tile is a tile that is purely decorative and has no collision.
    It inherits from `Tile`.
    """

    def __init__(self, game_map: GameMap, pos: tuple[int, int]) -> None:
        """Initialize the decorative tile."""
        super().__init__(game_map, pos)

        self.name = "Decorative Tile"

        self.is_collider = False

    def draw(self) -> None:
        """Draw the decorative tile."""
        self.surface.fill((10, 128, 10))
        super().draw()
