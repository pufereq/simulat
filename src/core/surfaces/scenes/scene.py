# -*- coding: utf-8 -*-
"""Scene module for simulat."""
from __future__ import annotations

import pygame as pg
import logging as lg


class Scene:
    """Base class for scenes.

    A scene is a state of the game, e.g. the main menu, the game itself, the
    settings menu, etc. Each scene has its own class, which inherits from this
    class. The scenes are stored in the `scenes` dict in the `Simulat` class.
    A scene takes up the whole screen.
    """
    def __init__(self) -> None:
        """Initialize the scene."""
        from ...game import simulat
        self.id = type(self).__name__

        self.logger = lg.getLogger(f"{__name__}.{self.id}")

        self.logger.debug(f"Initializing scene {self.id}...")
        self.surface = pg.Surface((pg.display.Info().current_w,
                                   pg.display.Info().current_h))
        self.surface.fill((255, 255, 255))

        # show fallback message if Scene called directly
        if self.id == "Scene":
            text_surface = simulat.fonts["main"].render("FALLBACK SCENE",
                                                        True, (255, 0, 0))
            self.surface.blit(text_surface, (20, 20))

    def draw(self, screen):
        """Draw the scene to the screen."""
        screen.blit(self.surface, (0, 0))
