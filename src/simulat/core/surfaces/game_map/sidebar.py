# -*- coding: utf-8 -*-
"""Sidebar surface module."""

from __future__ import annotations

import logging as lg
import pygame as pg

from src.simulat.core.surfaces.surface import Surface


class Sidebar(Surface):
    """Sidebar class.

    The sidebar is a surface that is displayed on the right side of the game
    scene. It contains information about the game, the player, etc.
    """
    def __init__(self, scene: Scene) -> None:
        """Initialize the sidebar.

        Args:
            scene (Scene): The game scene.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.debug("Initializing sidebar surface...")

        self.scene = scene

        self.DISPLAY_SIZE = scene.size
        self.SIDEBAR_SIZE = (256, self.DISPLAY_SIZE[1])
        self.SIDEBAR_POS = (self.DISPLAY_SIZE[0] - self.SIDEBAR_SIZE[0], 0)

        # initialize time of day position
        self.tod_pos = 0
        self.tod_bar = pg.image.load("src/simulat/core/surfaces/scenes/game_scene/time_of_day.png").convert()
        self.tod_bar_pos = (8, 8)

        super().__init__(self.SIDEBAR_SIZE)

        self.surface.fill((0, 0, 0))

        self.add_text("Sidebar", ("center", "center"),
                      (255, 255, 255), "topbar")

        self.logger.debug(f"Sidebar size: {self.SIDEBAR_SIZE} px")

    def update(self) -> None:
        """Update the sidebar."""

    def render(self) -> None:
        """Render the sidebar."""
        pg.draw.rect(self.surface, "#000000", (7, 8,
                                               248, 10))
        self.blit(self.tod_bar, self.tod_bar_pos)
        pg.draw.rect(self.surface, "#afb0b6", (7 + self.tod_pos, 8,
                                               3, 10))

        self.scene.surface.blit(self.surface, self.SIDEBAR_POS)
