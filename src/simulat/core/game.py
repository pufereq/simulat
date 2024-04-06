# -*- coding: utf-8 -*-
"""Game module for simulat."""

from __future__ import annotations

import logging as lg
import sys
from typing import Final

import pygame as pg

from src.simulat.core import log_exception

# set up logging
lg.basicConfig(format="%(asctime)s : %(levelname)-8s : %(threadName)s : %(filename)s:"
               "%(lineno)d : %(name)s :: %(message)s",
               level=lg.DEBUG)

module_lg = lg.getLogger(__name__)


class Simulat:
    """Main class for simulat."""
    def __init__(self):
        """Initialize pygame and the main window."""
        # constants
        self.FPS: Final = 60
        self.SIZE: Final = (1280, 720)

        # set up logging
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.info("Starting simulat...")

        self.logger.debug("Initializing exception logging...")
        sys.excepthook = log_exception

        # initialize pygame
        self.logger.debug("Initializing pygame...")
        from src.simulat.core.version import VERSION

        pg.init()
        pg.display.set_caption(f"simulat {VERSION}")

        # initialize screen
        self.screen = pg.display.set_mode(self.SIZE)

        # initialize clock
        self.clock = pg.time.Clock()

    def _init_next(self):
        """Initialize fonts and scene handling."""
        # initialize fonts
        pg.font.init()
        self.fonts: dict[str, pg.font.Font] = {
            "main": pg.font.SysFont("monospace", 16),
            "topbar": pg.font.SysFont("monospace", 22),
            "button": pg.font.SysFont("monospace", 20),
        }

        # initialize focused surfaces
        from src.simulat.core.surfaces.scenes.scene import Scene
        from src.simulat.core.surfaces.surface import Surface
        self.focused_surfaces: list[Surface | Scene] = []

        # initialize topbar
        self._init_topbar()

        # initialize scenes
        self._init_scenes()

    def _init_topbar(self):
        """Initialize topbar."""
        from src.simulat.core.surfaces.topbar import Topbar
        from src.simulat.core.version import VERSION

        self.topbar = Topbar()
        self.topbar.update_debug(f"simulat {VERSION}")

    def _init_scenes(self):
        """Initialize scenes."""
        from .surfaces.scenes.game_scene.game_scene import GameScene
        from .surfaces.scenes.scene import Scene

        self.scenes: dict[str | None, Scene] = {}
        self.active_scene: str | None = None  # initial scene is defined in `run()`

        # fallback scene
        fallback_scene = Scene()
        self.scenes[None] = fallback_scene

        # main menu scene
        from .surfaces.scenes.main_menu_scene.main_menu_scene import \
            MainMenuScene
        main_menu_scene = MainMenuScene()
        self.scenes[main_menu_scene.id] = main_menu_scene

    def change_scene(self, scene_id: str) -> None:
        """Change the active scene.

        Args:
            scene_id (str): The id of the scene to change to
                (from `self.scenes`)
        """
        self.logger.info(f"Changing scene to {scene_id}...")

        # unfocus current scene
        self.unfocus_surface(self.scenes[self.active_scene])

        # change scene
        self.active_scene = scene_id

        # focus new scene
        self.focus_surface(self.scenes[self.active_scene])

        # update topbar title
        self.topbar.update_title(scene_id)

    def focus_surface(self, surface: Surface) -> None:
        """Focus a surface."""
        if surface not in self.focused_surfaces:
            self.focused_surfaces.append(surface)
            self.logger.debug(f"Focused surface {surface}.")

    def unfocus_surface(self, surface: Surface,
                        supress_error: bool = True) -> None:
        """Unfocus a surface."""
        try:
            self.focused_surfaces.remove(surface)
        except ValueError as e:
            if not supress_error:
                raise e
            self.logger.warning(f"Surface {surface} not focused. Skipping...")
        else:
            self.logger.debug(f"Unfocused surface {surface}.")

    def run(self):
        from src.simulat.core.version import VERSION
        self.running: bool = True
        self.frame_delta: float = 1  # this avoids exceptions on first frame

        self.logger.info("Starting main loop...")
        self.change_scene("MainMenuScene")  # initial scene
        while self.running:
            # PROCESS EVENTS / INPUT
            # check for key events
            events = pg.event.get()
            keys = pg.key.get_pressed()

            # check for window events
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill((30, 30, 30))

            if keys[pg.K_ESCAPE]:
                self.running = False

            for surface in self.focused_surfaces:  # copy to avoid RuntimeError
                surface.input(events=events, keys=keys,
                              mouse_pos=pg.mouse.get_pos(),
                              mouse_buttons=pg.mouse.get_pressed())

            # UPDATE
            # update scene
            self.scenes[self.active_scene].update(self.frame_delta)

            # RENDER
            # draw scene
            self.scenes[self.active_scene].render(self.screen)

            # draw topbar
            self.screen.blit(self.topbar.surface, (0, 0))

            pg.display.set_caption(f"simulat {VERSION} - FPS: {self.clock.get_fps():.2f}")

            # update screen
            pg.display.flip()

            # limit framerate
            self.frame_delta = self.clock.tick(self.FPS) * .001  # in seconds

        # quit pygame
        self.logger.info("Quit event received, exiting.")
        pg.quit()

    def quit(self):
        """Quit the game."""
        self.running = False


def init():
    """Initialize the game."""
    global simulat
    simulat = Simulat()
    simulat._init_next()
