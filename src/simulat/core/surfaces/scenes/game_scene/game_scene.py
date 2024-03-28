# -*- coding: utf-8 -*-
"""Game scene."""

from __future__ import annotations

import pygame as pg

from src.simulat.core.surfaces.game_map.game_map import GameMap
from src.simulat.core.surfaces.game_map.sidebar import Sidebar
from src.simulat.core.surfaces.scenes.scene import Scene
from src.simulat.core.surfaces.surface import Surface
from src.simulat.data.colors import BasicPalette, SimulatPalette


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

        # initialize corner overlay (rounded corners)
        self.corner_overlay = Surface(self.game_map.display_size)
        self.corner_overlay.surface.set_colorkey(BasicPalette.MAGENTA)
        self.corner_overlay.surface.fill(SimulatPalette.BACKGROUND)
        pg.draw.rect(
            self.corner_overlay.surface,
            BasicPalette.MAGENTA,
            (0, 0, *self.game_map.display_size),
            border_radius=8,
        )

    def update(self, delta: float) -> None:
        """Update the game scene.

        Args:
            delta (float): The time passed since the last frame.
        """
        self.game_map.update(delta)

    def render(self, dest) -> None:
        self.game_map.render()
        self.sidebar.render()

        self.surface.blit(
            self.corner_overlay.surface,
            (0, 0),
        )
        self.draw(dest)
