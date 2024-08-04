# -*- coding: utf-8 -*-
"""Main menu scene."""

from __future__ import annotations

import threading as th

import pygame as pg

from simulat.core.colors import BasicPalette, SimulatPalette
from simulat.core.game import simulat
from simulat.core.scenes.scene import Scene
from simulat.core.surfaces.buttons.button import Button
from simulat.core.surfaces.buttons.button_container import ButtonContainer
from simulat.core.time_it import Timer


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
        self.load_thread = th.Thread(
            name="Loading thread", target=self._load_game, daemon=True
        )

        self.button_container = ButtonContainer(
            self.surface,
            [
                Button(
                    "New Game", (193, 200), (256, 24), on_click=self._start_load_thread
                ),
                Button(
                    "Load Game", (193, 230), (256, 24), on_click=None, enabled=False
                ),
                Button("Settings", (193, 260), (124, 24), on_click=None, enabled=False),
                Button("Exit", (325, 260), (124, 24), on_click=simulat.quit),
            ],
        )

        self.surface.surface.fill(SimulatPalette.BACKGROUND)

        # add logo
        logo_path = "assets/logo/ingame/logo_menu.png"
        self.logo = pg.image.load(logo_path).convert_alpha()
        self.logo = pg.transform.scale(self.logo, (412, 82))

    def _load_game(self):
        from simulat.core.scenes.game_scene.game_scene import GameScene

        with Timer() as timer:
            simulat.scenes["GameScene"] = GameScene()
            simulat.change_scene("GameScene")
        self.logger.info(f"Took {timer.elapsed} s.")

    def _start_load_thread(self):
        if not self.load_thread.is_alive():
            self.button_container[0].enabled = False  # prevent multiple clicks
            self.load_thread.start()

    def input(
        self,
        *,
        events: list[pg.event.Event],
        keys: dict[int, bool],
        mouse_pos: tuple[int, int],
        mouse_buttons: tuple[bool, bool, bool],
    ) -> None:
        """Handle input events.

        Args:
            events (list[pg.event.Event]): List of pygame events.
            keys (dict[int, bool]): Dictionary of pressed keys.
        """

        # handle input for buttons
        self.button_container.input(
            events=events, keys=keys, mouse_pos=mouse_pos, mouse_buttons=mouse_buttons
        )

        # load the game map if the user presses enter, temporary before
        # main menu is implemented
        if keys[pg.K_RETURN]:
            # clear screen

            self.surface.surface.fill(SimulatPalette.BACKGROUND)
            # start loading thread only once
            if not self.load_thread.is_alive():
                self.load_thread.start()

    def render(self, dest) -> None:
        simulat.topbar.update_title("main menu")

        # draw logo
        self.surface.surface.blit(self.logo, (120, 100))

        # draw buttons
        self.button_container.render()

        if self.load_thread.is_alive():
            self.surface.fill(SimulatPalette.BACKGROUND)

        self.draw(dest)
