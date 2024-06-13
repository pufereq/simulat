# -*- coding: utf-8 -*-

from __future__ import annotations

import logging as lg

from src.simulat.core.scenes.game_scene.game_map.world import World


class DebugWorld(World):
    """Debug world class.

    A world for debugging purposes.
    """

    def __init__(self) -> None:
        """Initialize the debug world."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.info("Initializing debug world...")

        self.id: str = "simulat.world.debug_world"
        self.label: str = "Debug World"
        self.description: str = "A world for debugging purposes."

        self.layout: list[list[str]] = [
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#",],  # fmt: skip
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#",],  # fmt: skip
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#",],  # fmt: skip
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#",],  # fmt: skip
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#",],  # fmt: skip
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#",],  # fmt: skip
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#",],  # fmt: skip
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#",],  # fmt: skip
        ]

        for y, row in enumerate(self.layout):
            for x, tile_ch in enumerate(row):
                if tile_ch == "#":
                    tile_id = "simulat.tile.bricks"
                elif tile_ch == ".":
                    tile_id = "simulat.tile.grass"

                self.layout[y][x] = tile_id

        super().__init__(self.id, self.label, self.description, self.layout, (2, 2))

        self.logger.debug("Debug world initialized.")
