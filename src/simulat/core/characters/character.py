# -*- coding: utf-8 -*-
"""Character module."""

from __future__ import annotations

import logging as lg
from typing import Final

import pygame as pg
from src.simulat.core.surfaces.game_map.tiles.tile import (px_to_tiles,
                                                           tiles_to_px)

from src.simulat.core.surfaces.surface import Surface


class Character:
    """Character class.

    A character is an entity that can move on the game map. It can be a player,
    an enemy, an NPC, etc. Each character has its own class, which inherits
    from this class.
    """
    def __init__(self, game_map: GameMap, pos: tuple[float, float]) -> None:
        """Initialize the character.

        Args:
            game_map (GameMap): The game map.
            pos (tuple[float, float]): The character's position in tiles.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.first_name = "John"
        self.last_name = "Doe"
        self.name = f"{self.first_name} {self.last_name}"

        self.pos: list[float] = list(pos)  # position in tiles
        self.px_pos: list[int] = [tiles_to_px(pos[0]), tiles_to_px(pos[1])]

        self.max_speed: float = 4  # tiles per second

        self.velocity: list[float] = [0, 0]

        self.sprite = Surface((64, 64))

        self.sprite.fill((255, 255, 0))

        self.rect = self.sprite.surface.get_rect(center=pos)

        self.game_map = game_map

    def _cap_position(self) -> None:
        """Cap the character's position to the game map's size."""

        self.rect.x = max(
            min(self.rect.x, self.game_map.width - self.rect.width),
            0
        )
        self.rect.y = max(
            min(self.rect.y, self.game_map.height - self.rect.height),
            0
        )

    def update(self, delta: float) -> None:
        """Update the character.

        Args:
            delta (float): Time passed since the last update (in seconds).
        """
        self.move(
            self.velocity[0] * self.max_speed * delta,
            self.velocity[1] * self.max_speed * delta
        )

        # update px position
        self.px_pos = [tiles_to_px(self.pos[0]), tiles_to_px(self.pos[1])]
        self.rect.center = self.px_pos

        # cap position
        self._cap_position()

        # update tile position
        self.px_pos = self.rect.center
        self.pos = [px_to_tiles(self.px_pos[0]), px_to_tiles(self.px_pos[1])]

    def render(self) -> None:
        """Render the character."""
        from src.simulat.core.game import simulat
        # self.sprite.fill((255, 0, 0))
        self.game_map.blit(self.sprite.surface, self.rect)
        simulat.topbar.update_title(f"Character position: {self.pos}")

    def move(self, dx: float, dy: float) -> None:
        """Move the character.

        Args:
            dx (float): Horizontal distance to move (in tiles).
            dy (float): Vertical distance to move (in tiles).
        """

        # move horizontally
        if dx != 0:
            self.pos[0] += dx
            self.velocity[0] = 0

        # move vertically
        if dy != 0:
            self.pos[1] += dy
            self.velocity[1] = 0
