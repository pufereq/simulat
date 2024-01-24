# -*- coding: utf-8 -*-
"""Game scene."""

from __future__ import annotations

from ..scene import Scene
from .game_map import GameMap


class GameScene(Scene):
    """Game scene class.

    The game scene is the scene where the game takes place. It contains the
    game map, a sidebar, etc.
    """

    def __init__(self) -> None:
        """Initialize the game scene."""
        super().__init__()

        # initialize map
        self.game_map = GameMap()

    def update(self) -> None:
        """Update the game scene."""
        self.game_map.update()

    def render(self, dest) -> None:
        self.surface.blit(
            self.game_map.surface,
            (0, 0),
            self.game_map.camera
        )
        self.draw(dest)
