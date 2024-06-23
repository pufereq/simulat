# -*- coding: utf-8 -*-
"""Entity module."""

from __future__ import annotations

import logging as lg

import pygame as pg

from src.simulat.core.scenes.game_scene.game_map.tiles.map_tile import MapTile
from src.simulat.core.scenes.game_scene.game_map.tiles.tile_type import (
    px_to_tiles,
    tiles_to_px,
)
from src.simulat.core.scenes.game_scene.game_map.world import World
from src.simulat.core.surfaces.surface import Surface


class Entity:
    """Entity class.

    An entity is an object that can move on the game map. It can be a player,
    an enemy, an NPC, etc. Each entity has its own class, which inherits
    from this class.
    """

    def __init__(
        self,
        world: World,
        pos: tuple[float, float],
        size: tuple[float, float],
        size_unit: str,
        *,
        can_collide: bool = True,
    ) -> None:
        """Initialize the entity.

        Args:
            world (World): The world.
            pos (tuple[float, float]): The Entity's position in tiles.
            size (tuple[float, float]): The Entity's size.
            size_unit (str): The unit of the Entity's size ("tiles" OR "px").
            can_collide (bool): Whether the Entity can collide with
            collider tiles.

        Raises:
            ValueError: If the unit is invalid.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        if size_unit not in ("tiles", "px"):
            raise ValueError(f"Invalid unit: {size_unit}")

        self.first_name: str = "John"
        self.last_name: str = "Doe"

        self.pos: list[float] = list(pos)  # position in tiles

        if size_unit == "px":
            self.px_size: tuple[float, float] = size
            self.size: tuple[float, float] = (
                px_to_tiles(size[0]),
                px_to_tiles(size[1]),
            )
        elif size_unit == "tiles":
            self.size: tuple[float, float] = size
            self.px_size: tuple[float, float] = (
                tiles_to_px(size[0]),
                tiles_to_px(size[1]),
            )

        self.logger.debug(
            f"Initializing entity {type(self).__name__} " f"at {self.pos}..."
        )

        self.can_collide: bool = can_collide

        self.max_speed: float = 4  # tiles per second

        self.velocity: list[float] = [0, 0]

        self.sprite = Surface(self.px_size)

        self.sprite.fill((255, 255, 0))

        self.rect = pg.Rect(
            self.px_pos,
            self.px_size,
        )

        self.world = world

    @property
    def name(self) -> str:
        """str: The entity's full name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def px_pos(self) -> tuple[int, int]:
        """list[int]: The entity's position in pixels."""
        return (tiles_to_px(self.pos[0]), tiles_to_px(self.pos[1]))

    @px_pos.setter
    def px_pos(self, value: tuple[int, int]) -> None:
        self.pos = [px_to_tiles(value[0]), px_to_tiles(value[1])]

    @property
    def current_chunk(self) -> tuple[int, int]:
        return (
            int(self.pos[0] // self.world.CHUNK_SIZE),
            int(self.pos[1] // self.world.CHUNK_SIZE),
        )

    @property
    def pos_in_chunk(self) -> tuple[int, int]:
        return (
            int(self.pos[0] % self.world.CHUNK_SIZE),
            int(self.pos[1] % self.world.CHUNK_SIZE),
        )

    @property
    def current_tile(self) -> MapTile | None:
        """MapTile: The tile the entity is currently on."""
        try:
            return self.world.chunk_map[self.current_chunk][self.pos_in_chunk]
        except KeyError:
            return None

    @property
    def current_speed(self) -> float:
        """float: The entity's current speed."""
        return self.max_speed * (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5

    def _cap_position(self, pos_tiles: tuple[float, float]) -> None:
        """Cap the entity's position to the game map's size."""
        # covert to top-left position
        topleft_pos = (pos_tiles[0] - self.size[0] / 2, pos_tiles[1] - self.size[1] / 2)

        # cap position
        x = max(min(topleft_pos[0], self.world.size[0] - self.size[0]), 0)
        y = max(min(topleft_pos[1], self.world.size[1] - self.size[1]), 0)

        # convert back to center position
        self.pos = [x + self.size[0] / 2, y + self.size[1] / 2]

    def _check_collision(self, x: float, y: float) -> list[MapTile]:
        """Check if the entity collides with a collider tile.

        Args:
            x (float): Horizontal distance to move (in tiles).
            y (float): Vertical distance to move (in tiles).

        Returns:
            list[MapTile]: The colliding tiles.
        """
        x, y = tiles_to_px(x), tiles_to_px(y)
        new_pos_rect = self.rect.copy()
        new_pos_rect.center = (x, y)
        colliding: list[MapTile] = []
        for tile in self.world.collidables.values():
            if new_pos_rect.colliderect(tile.rect):
                colliding.append(tile)
        return colliding

    def update(self, delta: float) -> None:
        """Update the entity.

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
        # self._cap_position(self.pos)

        # update px position
        self.rect.center = self.px_pos

    def render(self, surface: Surface) -> None:
        """Render the entity.

        Args:
            surface (Surface): The surface to render the Entity on.
        """
        surface.blit(
            self.sprite.surface,
            (
                self.px_pos[0] - self.world.player.px_pos[0] + surface.width // 2,
                self.px_pos[1] - self.world.player.px_pos[1] + surface.height // 2,
            ),
        )

    def move(self, dx: float, dy: float) -> None:
        """Move the entity.

        Args:
            dx (float): Horizontal distance to move (in tiles).
            dy (float): Vertical distance to move (in tiles).
        """

        # check collision
        colliding_x = self._check_collision(self.pos[0] + dx, self.pos[1])
        new_pos_x = self.pos[0] + dx

        if colliding_x:
            for tile in colliding_x:
                if dx > 0:
                    new_pos_x = px_to_tiles(tile.rect.left) - self.size[0] / 2
                elif dx < 0:
                    new_pos_x = px_to_tiles(tile.rect.right) + self.size[0] / 2

        if dx != 0:
            self.move_to(new_pos_x, self.pos[1])

        colliding_y = self._check_collision(self.pos[0], self.pos[1] + dy)
        new_pos_y = self.pos[1] + dy

        if colliding_y:
            for tile in colliding_y:
                if dy > 0:
                    new_pos_y = px_to_tiles(tile.rect.top) - self.size[1] / 2
                elif dy < 0:
                    new_pos_y = px_to_tiles(tile.rect.bottom) + self.size[1] / 2
        if dy != 0:
            self.move_to(self.pos[0], new_pos_y)

    def move_to(self, x: float, y: float) -> None:
        """Move the entity to a specific position.

        Args:
            x (float): The x-coordinate of the position to move to (in tiles).
            y (float): The y-coordinate of the position to move to (in tiles).
        """
        self.pos = [x, y]
        self.velocity = [0, 0]
        # self.rect.center = self.px_pos
