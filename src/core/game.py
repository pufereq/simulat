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
        self.screen = pg.display.set_mode((1280, 720),
                                          pg.RESIZABLE | pg.SCALED)

        # initialize clock
        self.clock = pg.time.Clock()

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