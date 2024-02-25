# -*- coding: utf-8 -*-
"""Game scene."""

from __future__ import annotations

import pygame as pg

from src.simulat.core.surfaces.game_map.game_map import GameMap
from src.simulat.core.surfaces.game_map.sidebar import Sidebar
from src.simulat.core.surfaces.scenes.scene import Scene
from src.simulat.core.surfaces.surface import Surface


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
        self.corner_overlay.surface.set_colorkey((255, 0, 255))
        pg.draw.rect(
            self.corner_overlay.surface,
            (255, 0, 255),
            (0, 0, *self.game_map.display_size),
            border_radius=8,
        )

        # initialize lighting overlay
        self.lighting_overlay = Surface(self.game_map.display_size)
        self.lighting_overlay.surface.fill("#000000")

    def update(self, delta: float) -> None:
        """Update the game scene.

        Args:
            delta (float): The time passed since the last frame.
        """
        from src.simulat.core.game import simulat
        night_light = 245

        # 05:00 - 06:00 -- dawn
        # 06:00 - 18:00 -- day
        # 18:00 - 19:00 -- dusk
        # 19:00 - 05:00 -- night
        # time_s -- minutes since 06:00

        # dawn
        if 300 <= simulat.time_s < 360:  # 05:00 - 06:00
            lighting_alpha = night_light - (simulat.time_s - 300) / 60 * 255
        # day
        elif 360 <= simulat.time_s < 1080:  # 06:00 - 18:00
            lighting_alpha = 0
        # dusk
        elif 1080 <= simulat.time_s < 1140:  # 18:00 - 19:00
            lighting_alpha = (simulat.time_s - 1080) / 60 * night_light
        # night
        elif 1140 <= simulat.time_s or simulat.time_s < 300:  # 19:00 - 05:00
            lighting_alpha = night_light

        self.lighting_overlay.surface.set_alpha(lighting_alpha)

        self.sidebar.tod_pos = (simulat.time_s) / 1440 * 240

        self.sidebar.update()
        self.game_map.update(delta)

    def render(self, dest) -> None:
        self.game_map.render()
        self.sidebar.render()

        self.surface.blit(
            self.corner_overlay.surface,
            (0, 0),
        )

        self.surface.blit(
            self.lighting_overlay.surface,
            (0, 0),
        )

        self.draw(dest)
