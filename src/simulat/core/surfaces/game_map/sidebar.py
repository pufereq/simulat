# -*- coding: utf-8 -*-
"""Sidebar surface module."""

from __future__ import annotations

import logging as lg

from src.simulat.core.surfaces.surface import Surface
from src.simulat.data.colors import SimulatPalette


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

        self.PARENT_POS = scene.pos
        self.PARENT_SIZE = scene.size
        self.SIDEBAR_SIZE = (128, self.PARENT_SIZE[1])
        self.ABSOLUTE_SIDEBAR_POS = (self.PARENT_SIZE[0] - self.SIDEBAR_SIZE[0], 24)
        self.RELATIVE_SIDEBAR_POS = (self.ABSOLUTE_SIDEBAR_POS[0], 0)

        super().__init__(self.SIDEBAR_SIZE, self.ABSOLUTE_SIDEBAR_POS)

        self.surface.fill(SimulatPalette.BACKGROUND)

        self.add_text("Sidebar", ("center", "center"), font="topbar")

        self.logger.debug(f"Sidebar size: {self.SIDEBAR_SIZE} px")

    def update(self) -> None:
        """Update the sidebar."""
        pass

    def render(self) -> None:
        """Render the sidebar."""
        self.scene.surface.blit(self.surface, self.RELATIVE_SIDEBAR_POS)
