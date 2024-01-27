# -*- coding: utf-8 -*-
"""Scene module for simulat."""
from __future__ import annotations

import logging as lg

import pygame as pg

from src.simulat.core.surfaces.surface import Surface


class Scene:
    """Base class for scenes.

    A scene is a state of the game, e.g. the main menu, the game itself, the
    settings menu, etc. Each scene has its own class, which inherits from this
    class. The scenes are stored in the `scenes` dict in the `Simulat` class.
    A scene takes up the whole screen (minus the topbar).
    """
    def __init__(self) -> None:
        """Initialize the scene."""
        from ...game import simulat
        self.id = type(self).__name__

        self.logger = lg.getLogger(f"{__name__}.{self.id}")

        self.logger.debug(f"Initializing scene {self.id}...")
        self.size = (simulat.SIZE[0], simulat.SIZE[1] - simulat.topbar.height)
        self.surface = Surface(
            self.size,
            (0, simulat.topbar.height)
        )

        self.surface.fill((255, 255, 255))

        # show fallback message if Scene called directly
        if self.id == "Scene":
            self.logger.warning("`Scene` called directly, "
                                "showing fallback message...")
            self.surface.add_text(
                "FALLBACK SCENE",
                (20, 20),
                (255, 0, 0)
            )

    def update(self) -> None:
        """Update the scene."""
        pass

    def render(self, dest) -> None:
        """Render the scene."""
        self.draw(dest)

    def draw(self, screen: pg.Surface):
        """Draw the scene to the screen."""
        screen.blit(self.surface.surface, self.surface.pos)
