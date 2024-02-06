# -*- coding: utf-8 -*-
"""Character module."""

from __future__ import annotations

import logging as lg
from typing import Final

import pygame as pg
from src.simulat.core.surfaces.game_map.tiles.tile import px_to_tiles, tiles_to_px

from src.simulat.core.surfaces.surface import Surface


class Character:
    """Character class.

    A character is an entity that can move on the game map. It can be a player,
    an enemy, an NPC, etc. Each character has its own class, which inherits
    from this class.
    """
    def __init__(self, game_map: GameMap, pos: list[int]) -> None:
        """Initialize the character."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.first_name = "John"
        self.last_name = "Doe"
        self.name = f"{self.first_name} {self.last_name}"

        self.px_pos: list[int] = pos
        self.max_speed: float = 16
        self.speed: float = 0

        self.velocity: list[float] = [0, 0]

        self.sprite = Surface((64, 64))

        self.sprite.fill((255, 255, 0))

        self.rect = self.sprite.surface.get_rect(center=pos)

        self.game_map = game_map

    def update(self) -> None:
        """Update the character."""
        self.px_pos = (tiles_to_px(self.pos[0]), tiles_to_px(self.pos[1]))
        self.rect.center = self.px_pos
        self.speed = min(self.max_speed, self.speed + 1)
        self.move(
            self.velocity[0] * self.max_speed,
            self.velocity[1] * self.max_speed
        )
        self.px_pos = self.rect.center
        self.pos = tuple(px_to_tiles(idx, False) for idx in self.px_pos)

    def render(self) -> None:
        """Render the character."""
        from src.simulat.core.game import simulat
        # self.sprite.fill((255, 0, 0))
        self.game_map.blit(self.sprite.surface, self.rect)
        simulat.topbar.update_title(f"Character position: {self.pos}")

    def move(self, dx: float, dy: float) -> None:
        """Move the character.

        Args:
            dx (float): Horizontal distance to move.
            dy (float): Vertical distance to move.
        """

        # move horizontally
        if dx != 0:
            self.px_pos[0] += dx
            self.px_pos[0] = max(0, min(self.game_map.MAP_SIZE[0] - 1,
                                        self.px_pos[0]))
            self.velocity[0] = 0

        # move vertically
        if dy != 0:
            self.px_pos[1] += dy
            self.px_pos[1] = max(0, min(self.game_map.MAP_SIZE[1] - 1,
                                        self.px_pos[1]))
            self.velocity[1] = 0

        self.speed = 0
