# -*- coding: utf-8 -*-
"""Camera module."""

from __future__ import annotations

import logging as lg

import pygame as pg

import math

from src.simulat.core.game import simulat
from src.simulat.core.surfaces.game_map.tiles.tile import tiles_to_px


class Camera():
    """Camera class.

    The camera is a pygame.Rect object that represents the part of the game map
    that is currently visible on the screen. It can be moved around the game
    map.
    """

    def __init__(self, game_map: GameMap) -> None:
        """Initialize the camera."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.debug("Initializing camera...")

        self.game_map = game_map

        self.rect = pg.Rect((0, 0), self.game_map.display_size)

        self.speed: int = tiles_to_px(0.25)
        self.actual_speed: float = 0

        self.velocity: list[float] = [0, 0]
        self.max_velocity: float = 1

        self.logger.debug(f"Camera size: {self.rect.size} px")

        self.logger.debug("Camera initialized.")

    def move(self, dx: float, dy: float) -> None:
        """Move the camera by the given offset."""
        self.rect.x += int(dx)
        self.rect.y += int(dy)

    def move_to(self, pos: tuple[int, int]) -> None:
        """Move the camera to the given position."""
        self.rect.center = pos

    def update(self) -> None:
        """Update the camera."""
        # So... I have spent a lot of time on the camera movement, and I have
        # just realized that it is not necessary at all. The camera is just a
        # centered rect that follows the player... I will keep the methods
        # though, they might be useful later.

        self.move_to(self.game_map.player.rect.center)

        self._cap_camera()

    def _cap_camera(self) -> None:
        """Cap the camera to the game map."""
        self.rect.x = max(
            min(self.rect.x, self.game_map.width - self.rect.width),
            0
        )
        self.rect.y = max(
            min(self.rect.y, self.game_map.height - self.rect.height),
            0
        )

    def _decay_velocity(self) -> None:
        """Decay the camera velocity."""
        friction = 0.75
        self.velocity[0] *= friction
        self.velocity[1] *= friction

    def _normalize_velocity(self) -> None:
        """Normalize the camera velocity."""
        self.actual_speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)

        # prevent moving faster diagonally
        if self.actual_speed > self.max_velocity:
            self.velocity[0] /= self.actual_speed
            self.velocity[1] /= self.actual_speed
            self.actual_speed = self.max_velocity

        # prevent endless deceleration
        if round(self.actual_speed, 2) == 0:
            self.velocity[0] = 0
            self.velocity[1] = 0
            self.actual_speed = 0
        self.actual_speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        pass
