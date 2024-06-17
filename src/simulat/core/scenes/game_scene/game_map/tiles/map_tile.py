# -*- coding: utf-8 -*-

from __future__ import annotations

import logging as lg
import math

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

    instances: int = 0

    def __init__(self, position: tuple[int, int], tile_id: str) -> None:
        """Initialize the map tile.

        Args:
            position (tuple[int, int]): The position of the tile in tiles.
            tile_id (str): The ID of the tile type.
        """
        MapTile.instances += 1
        from src.simulat.core.scenes.game_scene.game_map.tiles.tile_manager import (
            id_to_tile,
        )

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.instance_num = MapTile.instances

        self.pos = position
        self.px_pos = (tiles_to_px(self.pos[0]), tiles_to_px(self.pos[1]))

        self.tile_type: TileType = id_to_tile(tile_id)
        self.texture = self._get_random_texture(self.tile_type.textures)

        self.rect = pg.Rect(
            self.px_pos,
            (TILE_SIZE, TILE_SIZE),
        )

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.pos}, {self.tile_type.id})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.pos}, {self.tile_type.id})"

    def _get_random_texture(self, texture_list: list[pg.Surface]) -> pg.Surface:
        """Get a random texture from the tile type textures based on instance_num.

        Returns:
            pg.Surface: A random texture from the tile type textures.
        """
        random = round(math.tan(self.instance_num))

        return texture_list[random % len(texture_list)]

    def draw(self, surface: Surface, pos: tuple[int, int]) -> None:
        """Draw the map tile on the surface.

        Args:
            surface (Surface): The surface to draw the map tile on.
            pos (tuple[int, int]): The position to draw the map tile at.
        """
        surface.blit(self.texture, pos)
