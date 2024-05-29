# -*- coding: utf-8 -*-
"""Character module."""

from __future__ import annotations

import logging as lg

from src.simulat.core.surfaces.game_map.tiles.tile import Tile, px_to_tiles, tiles_to_px
from src.simulat.core.surfaces.surface import Surface


class Character:
    """Character class.

    A character is an entity that can move on the game map. It can be a player,
    an enemy, an NPC, etc. Each character has its own class, which inherits
    from this class.
    """

    def __init__(
        self,
        game_map: GameMap,
        pos: tuple[float, float],
        size: tuple[float, float],
        unit: str,
        *,
        can_collide: bool = True,
    ) -> None:
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
            self.size: tuple[float, float] = (
                px_to_tiles(size[0]),
                px_to_tiles(size[1]),
            )
        elif unit == "tiles":
            self.size: tuple[float, float] = size
            self.px_size: tuple[float, float] = (
                tiles_to_px(size[0]),
                tiles_to_px(size[1]),
            )

        self.logger.debug(
            f"Initializing character {type(self).__name__} " f"at {self.pos}..."
        )

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

    def _cap_position(self, pos_tiles: tuple[float, float]) -> None:
        """Cap the character's position to the game map's size."""
        # covert to top-left position
        topleft_pos = (pos_tiles[0] - self.size[0] / 2, pos_tiles[1] - self.size[1] / 2)

        # cap position
        x = max(min(topleft_pos[0], self.game_map.MAP_SIZE[0] - self.size[0]), 0)
        y = max(min(topleft_pos[1], self.game_map.MAP_SIZE[1] - self.size[1]), 0)

        # convert back to center position
        self.pos = [x + self.size[0] / 2, y + self.size[1] / 2]

    def _check_collision(self, x: float, y: float) -> Tile | None:
        """Check if the character collides with a collider tile.

        Args:
            x (float): Horizontal distance to move (in tiles).
            y (float): Vertical distance to move (in tiles).

        Returns:
            Tile | None: The collider tile the character collides with.
        """
        x, y = tiles_to_px(x), tiles_to_px(y)
        new_pos_rect = self.rect.copy()
        new_pos_rect.center = (x, y)
        for tile in self.game_map.collider_tiles:
            if new_pos_rect.colliderect(tile.rect):
                return tile
        return None

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
            self.velocity[1] * self.max_speed * delta,
        )

        # cap position
        self._cap_position(self.pos)

        # update px position
        self.rect.center = self.px_pos

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
        collider_x = self._check_collision(self.pos[0] + dx, self.pos[1])
        if collider_x and self.can_collide:
            # teleport the player to the left or right of the collider tile
            if dx < 0:
                new_pos_x = px_to_tiles(collider_x.rect.right) + self.size[0] / 2
            elif dx > 0:
                new_pos_x = px_to_tiles(collider_x.rect.left) - self.size[0] / 2
            if dx != 0:
                self.move_to(new_pos_x, self.pos[1])
                dx = 0

        collider_y = self._check_collision(self.pos[0], self.pos[1] + dy)
        if collider_y and self.can_collide:
            # teleport the player to the top or bottom of the collider tile
            if dy < 0:
                new_pos_y = px_to_tiles(collider_y.rect.bottom) + self.size[1] / 2
            elif dy > 0:
                new_pos_y = px_to_tiles(collider_y.rect.top) - self.size[1] / 2
            if dy != 0:
                self.move_to(self.pos[0], new_pos_y)
                dy = 0
        # move horizontally
        if dx != 0:
            self.move_to(self.pos[0] + dx, self.pos[1])

        # move vertically
        if dy != 0:
            self.move_to(self.pos[0], self.pos[1] + dy)

    def move_to(self, x: float, y: float) -> None:
        """Move the character to a specific position.

        Args:
            x (float): The x-coordinate of the position to move to (in tiles).
            y (float): The y-coordinate of the position to move to (in tiles).
        """
        self.pos = [x, y]
        self.velocity = [0, 0]
        # self.rect.center = self.px_pos
