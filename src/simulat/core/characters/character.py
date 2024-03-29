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
    def __init__(self, game_map: GameMap, pos: tuple[float, float],
                 size: tuple[float, float], unit: str, *,
                 can_collide: bool = True) -> None:
        """Initialize the character.

        Args:
            game_map (GameMap): The game map.
            pos (tuple[float, float]): The character's position in tiles.
            size (tuple[float, float]): The character's size.
            unit (str): The unit of the character's size ("tiles" OR "px").
            can_collide (bool): Whether the character can collide with
            collider tiles.

        Raises:
            ValueError: If the unit is invalid.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        if unit not in ("tiles", "px"):
            raise ValueError(f"Invalid unit: {unit}")

        self.first_name: str = "John"
        self.last_name: str = "Doe"

        self.pos: list[float] = list(pos)  # position in tiles

        if unit == "px":
            self.px_size: tuple[float, float] = size
            self.size: tuple[float, float] = (px_to_tiles(size[0]),
                                              px_to_tiles(size[1]))
        elif unit == "tiles":
            self.size: tuple[float, float] = size
            self.px_size: tuple[float, float] = (tiles_to_px(size[0]),
                                                  tiles_to_px(size[1]))

        self.logger.debug(f"Initializing character {type(self).__name__} "
                          f"at {self.pos}...")

        self.can_collide: bool = can_collide

        self.max_speed: float = 4  # tiles per second

        self.velocity: list[float] = [0, 0]

        self.sprite = Surface(self.px_size)

        self.sprite.fill((255, 255, 0))

        self.rect = self.sprite.surface.get_rect(center=self.px_pos)

        self.game_map = game_map

    @property
    def name(self) -> str:
        """str: The character's full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def px_pos(self) -> tuple[int, int]:
        """list[int]: The character's position in pixels."""
        return (tiles_to_px(self.pos[0]), tiles_to_px(self.pos[1]))

    @property
    def current_speed(self) -> float:
        """float: The character's current speed."""
        return self.max_speed * (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5

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

        # normalize diagonal movement
        if self.velocity[0] != 0 and self.velocity[1] != 0:
            self.velocity[0] *= 0.7071
            self.velocity[1] *= 0.7071

        self.move(
            self.velocity[0] * self.max_speed * delta,
            self.velocity[1] * self.max_speed * delta
        )

        # update px position
        self.rect.center = self.px_pos

        # cap position
        self._cap_position()

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
        if self._check_collision(self.pos[0] + dx, self.pos[1]) and self.can_collide:
            dx = 0
            # a sneaky hack to allow the player to touch the wall on lower
            # frame rates
            self.velocity[0] *= 0.5

        if self._check_collision(self.pos[0], self.pos[1] + dy) and self.can_collide:
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
