# -*- coding: utf-8 -*-
"""Game scene."""

from __future__ import annotations

import pygame as pg

from simulat.core.scenes.game_scene.game_map.sidebar import Sidebar
from simulat.core.scenes.scene import Scene


class GameScene(Scene):
    """Game scene class.

    The game scene is the scene where the game takes place. It contains the
    game map, a sidebar, etc.
    """

    def __init__(self) -> None:
        """Initialize the game scene."""
        super().__init__()

        # initialize sidebar
        self.sidebar = Sidebar(self)

        # initialize map
        from simulat.core.scenes.game_scene.game_map.game_map import GameMap

        self.game_map = GameMap(self)

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
        self.game_map.input(events=events, keys=keys)

    def update(self, delta: float) -> None:
        """Update the game scene.

        Args:
            delta (float): The time passed since the last frame.
        """
        self.game_map.update(delta)

    def render(self, dest) -> None:
        self.game_map.render()
        self.sidebar.render()

        self.draw(dest)
