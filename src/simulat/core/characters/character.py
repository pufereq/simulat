# -*- coding: utf-8 -*-
"""Character module."""

from __future__ import annotations

import logging as lg
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
        self.current_speed = 0

        self.sprite = Surface((64, 64))

        self.sprite.fill((255, 255, 0))

        self.rect = self.sprite.surface.get_rect(center=self.px_pos)

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

    def _check_collision(self, x: float, y: float) -> bool:
        """Check if the character collides with a collider tile.

        Args:
            x (float): Horizontal distance to move (in tiles).
            y (float): Vertical distance to move (in tiles).

        Returns:
            bool: True if the character collides with a collider tile, False
            otherwise.
        """
        x, y = tiles_to_px(x), tiles_to_px(y)
        for tile in self.game_map.collider_tiles:
            if tile.is_collider:
                new_pos_rect = self.rect.copy()
                new_pos_rect.center = (x, y)
                if new_pos_rect.colliderect(tile.rect):
                    return True
        return False

    def update(self, delta: float) -> None:
        """Update the character.

        Args:
            delta (float): Time passed since the last update (in seconds).
        """
        # cap velocity
        self.velocity[0] = max(min(self.velocity[0], 1), -1)
        self.velocity[1] = max(min(self.velocity[1], 1), -1)

        # update speed
        self.current_speed = self.max_speed * (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5

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
        self.game_map.character_surface.blit(self.sprite.surface, self.rect)

    def move(self, dx: float, dy: float) -> None:
        """Move the character.

        Args:
            dx (float): Horizontal distance to move (in tiles).
            dy (float): Vertical distance to move (in tiles).
        """

        # check for collision
        if self._check_collision(self.pos[0] + dx, self.pos[1]):
            dx = 0
            # a sneaky hack to allow the player to touch the wall on lower
            # frame rates
            self.velocity[0] *= 0.5

        if self._check_collision(self.pos[0], self.pos[1] + dy):
            dy = 0
            self.velocity[1] *= 0.5

        # move horizontally
        if dx != 0:
            self.pos[0] += dx
            self.velocity[0] = 0

        # move vertically
        if dy != 0:
            self.pos[1] += dy
            self.velocity[1] = 0
