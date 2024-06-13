# -*- coding: utf-8 -*-
"""Tile manager module for GameMap.

This module contains the tile manager, which is responsible for managing the
tiles used in the game map.
"""

from __future__ import annotations

import logging as lg
from typing import Any, Final

import yaml

from src.simulat.core.scenes.game_scene.game_map.tiles.tile_type import \
    TileType
from src.simulat.core.textures import get_texture

tiles: dict[str, TileType] = {}


def id_to_tile(tile_id: str) -> TileType:
    """Get a tile type by its ID."""
    return tiles[tile_id]


def initialize_tiles() -> None:
    """Initialize the tiles."""
    logger = lg.getLogger(f"{__name__}.{initialize_tiles.__name__}")
    tiles_path: Final[str] = "data/simulat/tiles.yml"

    # `missing` tile, used when a tile is not found
    missing_tile = {
        "id": "missing",
        "label": "Missing",
        "texture": "missing.png",
        "collision": False,
    }

    # load tiles from file
    with open(tiles_path, "r") as file:
        tiles_parsed: list[dict[str, Any]] | None = yaml.safe_load(file)
        if tiles_parsed is None:
            logger.error(f"No tiles found in: {tiles_path}")
            tiles_parsed = []

    tiles_parsed.append(missing_tile)

    # initialize tiles
    for tile in tiles_parsed:
        tile_texture = get_texture(tile["texture"])
        tiles[tile["id"]] = TileType(
            tile["id"],
            tile["label"],
            tile_texture,
            tile["collision"],
        )
        logger.debug(f"Loaded tile {tile["id"]}")
