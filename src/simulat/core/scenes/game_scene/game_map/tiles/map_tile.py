# -*- coding: utf-8 -*-

from __future__ import annotations

import logging as lg

import pygame as pg

from src.simulat.core.scenes.game_scene.game_map.tiles.tile_type import (
    TILE_SIZE,
    TileType,
    tiles_to_px,
)
from src.simulat.core.surfaces.surface import Surface


class MapTile:
    """Map tile class.

    A map tile is a tile in a game map. It has a position and a tile type
    (see `TileType`).
    """

    def __init__(self, position: tuple[int, int], tile_id: str) -> None:
        """Initialize the map tile.

        Args:
            position (tuple[int, int]): The position of the tile in tiles.
            tile_id (str): The ID of the tile type.
        """
        from src.simulat.core.scenes.game_scene.game_map.tiles.tile_manager import (
            id_to_tile,
        )

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.pos = position
        self.px_pos = (tiles_to_px(self.pos[0]), tiles_to_px(self.pos[1]))

        self.tile_type: TileType = id_to_tile(tile_id)

        self.rect = pg.Rect(
            self.px_pos,
            (TILE_SIZE, TILE_SIZE),
        )

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.pos}, {self.tile_type.id})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.pos}, {self.tile_type.id})"

    def draw(self, surface: Surface, pos: tuple[int, int]) -> None:
        """Draw the map tile on the surface.

        Args:
            surface (Surface): The surface to draw the map tile on.
            pos (tuple[int, int]): The position to draw the map tile at.
        """
        surface.blit(self.texture, pos)
