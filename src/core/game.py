# -*- coding: utf-8 -*-
"""Game module for simulat."""

from __future__ import annotations

import pygame as pg
import logging as lg

# set up logging
lg.basicConfig(format="%(asctime)s - %(name)s:%(levelname)s - %(message)s",
               level=lg.DEBUG)

module_lg = lg.getLogger(__name__)
module_lg.setLevel(lg.DEBUG)


FPS: int = 60
SIZE: tuple[int, int] = (1280, 720)


class Simulat:
    """Main class for simulat."""
    def __init__(self):
        """Initialize pygame and the main window."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.info("Starting simulat...")

        # initialize pygame
        self.logger.debug("Initializing pygame...")
        pg.init()

        # initialize screen
        self.screen = pg.display.set_mode(SIZE)

        # initialize clock
        self.clock = pg.time.Clock()

    def _init_next(self):
        """Initialize fonts and scene handling."""
        # initialize fonts
        pg.font.init()
        self.fonts: dict[str, pg.font.Font] = {}
        self.fonts["main"] = pg.font.SysFont("monospace", 16)

        # initialize topbar
        self._init_topbar()

        # initialize scenes
        self._init_scenes()

    def _init_topbar(self):
        """Initialize topbar."""
        from src.core.surfaces.topbar import Topbar

        self.topbar = Topbar()

    def _init_scenes(self):
        """Initialize scenes."""
        from src.core.surfaces.scenes.scene import Scene

        self.scenes: dict[Scene] = {}
        self.scene: int | None = None

        # fallback scene
        fallback_scene = Scene()
        self.scenes[None] = fallback_scene

    def run(self):
        running: bool = True

        self.logger.info("Starting main loop...")
        while running:
            # check for window events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.screen.fill((30, 30, 30))

            # check for key events
            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                running = False

            # draw scene
            self.scenes[self.scene].draw(self.screen)

            # draw topbar
            self.screen.blit(self.topbar.surface, (0, 0))

            # update screen
            pg.display.flip()

            # limit framerate
            self.clock.tick(FPS)

        # quit pygame
        self.logger.info("Quit event received, exiting.")
        pg.quit()


def init():
    """Initialize the game."""
    global simulat
    simulat = Simulat()
    simulat._init_next()
