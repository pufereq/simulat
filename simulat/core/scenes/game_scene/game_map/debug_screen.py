# -*- coding: utf-8 -*-
"""Debug screen module for GameMap.

This module contains the debug screen, which is responsible for displaying information about the game.
"""

from __future__ import annotations

import logging as lg
import platform
from typing import Any

import pygame as pg

from simulat.core.colors import BasicPalette, SimulatPalette
from simulat.core.game import simulat
from simulat.core.scenes.game_scene.game_map.game_map import GameMap
from simulat.core.surfaces.surface import Surface


class DebugScreen:
    """Debug screen class.

    The debug screen is responsible for displaying information about the game.
    """

    def __init__(self, game_map: GameMap) -> None:
        """Initialize the debug screen.

        Args:
            game_map (GameMap): The game map.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.info("Initializing debug screen...")

        self.game_map: GameMap = game_map

        self.surface: Surface = Surface(self.game_map.viewport_size)
        # self.surface.surface.set_alpha(128)
        self.surface.surface.set_colorkey(BasicPalette.MAGENTA)
        self.visible: bool = False
        self.tiles_loaded: int = 0

    def render(self) -> None:
        """Render the debug screen."""

        world_data: list[str] = ["No world loaded"]
        tile_data: list[str] = ["Out of bounds"]

        # data requiring the world to be loaded
        if self.game_map.world is not None:
            # if None, the player is out of bounds
            if self.game_map.world.player.current_tile is not None:
                tile_data = [
                    f"Tile position: {self.game_map.world.player.current_tile.pos}",
                    f"Tile type: {self.game_map.world.player.current_tile.tile_type.id}",
                ]

            # set world data
            world_data = [
                f"World: {self.game_map.world.id}",
                f"Tiles: {self.tiles_loaded}/{len(self.game_map.world.chunk_map) * self.game_map.world.CHUNK_SIZE ** 2}",
                f"Chunks: {len(self.game_map.world.chunk_map)}",
                "",
                f"XY: {self.game_map.world.player.pos[0]:.4f} / {self.game_map.world.player.pos[1]:.4f}",
                f"Chunk: {self.game_map.world.player.current_chunk[0]} {self.game_map.world.player.current_chunk[1]} at {self.game_map.world.player.pos_in_chunk[0]} {self.game_map.world.player.pos_in_chunk[1]}",
                *tile_data,
            ]

        # structure of the debug screen
        self.structure: dict[str, list[str]] = {
            "left": [
                f"simulat {simulat.version}",
                f"{simulat.clock.get_fps():.0f} fps, {simulat.clock.get_time()} ms",
                "",
                *world_data,  # display world data
            ],
            "center": [],
            "right": [
                f"Python {platform.python_version()}",
                f"Pygame-ce {pg.version.ver}, SDL {pg.version.SDL}",
                f"Display: {simulat.DISPLAY_SIZE[0]}x{simulat.DISPLAY_SIZE[1]} (internal: {simulat.INTERNAL_SCREEN_SIZE[0]}x{simulat.INTERNAL_SCREEN_SIZE[1]})",
                "",
                f"{platform.platform()}",
            ],
        }

        # fill the surface with the background color
        self.surface.fill(BasicPalette.MAGENTA)

        # render the structure
        for side, content in self.structure.items():
            for i, line in enumerate(content):
                self.surface.blit_text(
                    line,
                    (0, 12 * i),
                    text_align=side,
                )

        self.game_map.surface.blit(self.surface.surface, (0, 0))
