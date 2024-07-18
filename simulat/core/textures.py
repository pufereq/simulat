# -*- coding: utf-8 -*-
"""Textures module.

This module contains the textures used in the game.
"""

from __future__ import annotations

import logging as lg
from functools import cache

import pygame as pg

from simulat.core.colors import BasicPalette
from simulat.core.scenes.game_scene.game_map.tiles.tile_type import TILE_SIZE

textures: dict[str, pg.Surface] = {}


@cache
def get_texture(relative_path: str) -> pg.Surface:
    """Load textures.

    Args:
        relative_path (str): The path to the texture (relative to `assets/textures/`).
    """
    logger = lg.getLogger(f"{__name__}.{get_texture.__name__}")
    path = f"assets/textures/{relative_path}"
    try:
        texture = pg.image.load(path)
        texture = pg.transform.scale(texture, (TILE_SIZE, TILE_SIZE))
        return texture
    except FileNotFoundError:
        logger.error(f"Error loading texture: {path}")
        # draw a black-magenta checkerboard
        null_texture = pg.Surface((2, 2))
        null_texture.fill(BasicPalette.BLACK)
        null_texture.fill(BasicPalette.MAGENTA, (1, 0, 1, 1))
        null_texture.fill(BasicPalette.MAGENTA, (0, 1, 1, 1))
        null_texture = pg.transform.scale(null_texture, (TILE_SIZE, TILE_SIZE))
        return null_texture
