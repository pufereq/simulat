# -*- coding: utf-8 -*-
"""Main menu scene."""

from __future__ import annotations

import threading as th

import pygame as pg

from src.simulat.core.surfaces.scenes.scene import Scene
from src.simulat.core.time_it import Timer
from src.simulat.data.colors import BasicPalette, SimulatPalette


class MainMenuScene(Scene):
    """Main menu scene class.

    The main menu scene is the scene where the game starts. It contains the
    main menu, the settings menu, etc.
    """

    def __init__(self) -> None:
        """Initialize the main menu scene.

        The main menu scene is the first scene that is displayed when the game
        starts. It contains the main menu, the settings menu, etc.
        """
        super().__init__()

        # initialize the loading thread
        self.load_thread = th.Thread(name="Loading thread",
                                     target=self._load_game, daemon=True)

        self.surface.surface.fill(SimulatPalette.BACKGROUND)

    def input(self, *, events: list[pg.event.Event], keys: dict[int, bool]) -> None:
        """Handle input events.

        Args:
            events (list[pg.event.Event]): List of pygame events.
            keys (dict[int, bool]): Dictionary of pressed keys.
        """
        # load the game map if the user presses enter, temporary before
        # main menu is implemented
        if keys[pg.K_RETURN]:
            # draw loading screen
            self.surface.add_text("Loading...", ("center", "center"),
                                  color=BasicPalette.WHITE)

            # start loading thread only once
            if not self.load_thread.is_alive():
                self.load_thread.start()

    def _load_game(self):
        from src.simulat.core.game import simulat
        from src.simulat.core.surfaces.scenes.game_scene.game_scene import \
            GameScene

        with Timer() as timer:
            simulat.scenes["GameScene"] = GameScene()
            simulat.change_scene("GameScene")
        self.logger.info(f"Took {timer.elapsed} s.")

    def render(self, dest) -> None:
        from src.simulat.core.game import simulat
        simulat.topbar.update_title("main menu")
        self.draw(dest)
