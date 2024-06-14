# -*- coding: utf-8 -*-
"""Tile module for GameMap."""

from __future__ import annotations

import logging as lg
from typing import Final

import pygame as pg

from src.simulat.core.surfaces.surface import Surface

TILE_SIZE: Final = 32  # pixels


class TileType:
    """Tile type class.

    A tile type is a type of tile that can be used in a map. It has an ID, a
    label, a texture, and a collision property.
    """

    def __init__(
        self, _id: str, label: str, textures: list[pg.Surface], collision: bool
    ) -> None:
        """Initialize the tile type.

        Args:
            _id (str): The tile type's ID.
            label (str): The tile type's label.
            textures (list[pg.Surface]): The tile type's texture.
            collision (bool): The tile type's collision property.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.id = _id
        self.label = label
        self.textures = textures
        self.collision = collision

        self.logger.debug(f"Initialized tile type: {self}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.id=}, {self.label=}, {self.textures=}, {self.collision=})"

    def __str__(self) -> str:
        return f"{self.label} ({self.id})"

    def draw(self, surface: Surface, pos_tiles: tuple[int, int]) -> None:
        """Draw the tile type on the surface.

        Args:
            surface (Surface): The surface to draw the tile type on.
            pos_tiles (tuple[int, int]): The position of the tile in tiles.
        """
        surface.blit(
            self.texture, (tiles_to_px(pos_tiles[0]), tiles_to_px(pos_tiles[1]))
        )


def tiles_to_px(tiles: int | float) -> int:
    """Convert tiles to pixels."""
    return round(tiles * TILE_SIZE)


def px_to_tiles(px: int) -> float:
    """Convert pixels to tiles."""
    return px / TILE_SIZE
