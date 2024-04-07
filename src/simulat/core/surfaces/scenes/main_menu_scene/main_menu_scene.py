# -*- coding: utf-8 -*-
"""Main menu scene."""

from __future__ import annotations

import threading as th

import pygame as pg

from src.simulat.core.game import simulat
from src.simulat.core.surfaces.buttons.button import Button
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
        self.game_map_loading_progress: dict = {
            "task": "Loading...",
            "progress": 0.0
        }

        # initialize the loading thread
        self.load_thread = th.Thread(name="Loading thread",
                                     target=self._load_game, daemon=True)

        self.buttons: list[Button] = [
            Button("New Game", (386, 400), (512, 48),
                   on_click=self._start_load_thread),

            Button("Load Game", (386, 464), (512, 48),
                   on_click=None, enabled=False),

            Button("Settings", (386, 528), (248, 48),
                   on_click=None, enabled=False),

            Button("Exit", (650, 528), (248, 48),
                   on_click=simulat.quit)
        ]

        self.surface.surface.fill(SimulatPalette.BACKGROUND)

        # add logo
        logo_path = "src/simulat/assets/logo/ingame/logo_menu.png"
        self.logo = pg.image.load(logo_path).convert_alpha()

    def _load_game(self):
        from src.simulat.core.surfaces.scenes.game_scene.game_scene import \
            GameScene

        with Timer() as timer:
            simulat.scenes["GameScene"] = GameScene()
            simulat.change_scene("GameScene")
        self.logger.info(f"Took {timer.elapsed} s.")

    def _start_load_thread(self):
        if not self.load_thread.is_alive():
            self.buttons[0].enabled = False  # prevent multiple clicks
            self.load_thread.start()

    def input(self, *, events: list[pg.event.Event], keys: dict[int, bool],
              mouse_pos: tuple[int, int],
              mouse_buttons: tuple[bool, bool, bool]) -> None:
        """Handle input events.

        Args:
            events (list[pg.event.Event]): List of pygame events.
            keys (dict[int, bool]): Dictionary of pressed keys.
        """

        # align mouse position with the surface position
        mouse_pos = (mouse_pos[0] - self.surface.pos_x,
                     mouse_pos[1] - self.surface.pos_y)

        # handle input for buttons
        for button in self.buttons:
            button.input(events=events, keys=keys, mouse_pos=mouse_pos,
                         mouse_buttons=mouse_buttons)

        # load the game map if the user presses enter, temporary before
        # main menu is implemented
        if keys[pg.K_RETURN]:
            # draw loading screen
            self.surface.surface.fill(SimulatPalette.BACKGROUND)
            self.surface.add_text("Loading...", ("center", "center"),
                                  color=BasicPalette.WHITE)

            # start loading thread only once
            if not self.load_thread.is_alive():
                self.load_thread.start()

    def render(self, dest) -> None:
        simulat.topbar.update_title("main menu")

        # draw logo
        self.surface.surface.blit(self.logo, (240, 200))

        # draw buttons
        for button in self.buttons:
            button.render(self.surface)

        if self.load_thread.is_alive():
            self.surface.fill(SimulatPalette.BACKGROUND)
            self.surface.add_text(
                f"{self.game_map_loading_progress['task']}"
                f" {self.game_map_loading_progress['progress']:.2f}%"
                if self.game_map_loading_progress['progress'] else "",
                ("center", "center")
            )
        self.draw(dest)
