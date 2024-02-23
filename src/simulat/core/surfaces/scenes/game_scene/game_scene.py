# -*- coding: utf-8 -*-
"""Game scene."""

from __future__ import annotations

from src.simulat.core.surfaces.game_map.game_map import GameMap
from src.simulat.core.surfaces.game_map.sidebar import Sidebar
from src.simulat.core.surfaces.scenes.scene import Scene


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
        self.game_map = GameMap(self)

    def update(self, delta: float) -> None:
        """Update the game scene.

        Args:
            delta (float): The time passed since the last frame.
        """
        self.game_map.update(delta)

    def render(self, dest) -> None:
        self.surface.blit(
            self.game_map.surface,
            (0, 0),
        )
        self.game_map.render()
        self.sidebar.render()
        self.draw(dest)
