# -*- coding: utf-8 -*-
"""Game map module for GameScene.

This module contains the game map, which is responsible for managing the game map in the game scene.
"""

from __future__ import annotations

import logging as lg
import math

import pygame as pg

from src.simulat.core.game import simulat
from src.simulat.core.scenes.game_scene.game_map.tiles.tile_manager import (
    initialize_tiles,
)
from src.simulat.core.scenes.game_scene.game_map.world import World
from src.simulat.core.scenes.game_scene.game_map.world_manager import (
    get_world,
    initialize_worlds,
)
from src.simulat.core.scenes.game_scene.game_scene import GameScene
from src.simulat.core.surfaces.surface import Surface


class GameMap:
    """Game map class.

    The game map is responsible for managing the game map in the game scene.
    """

    def __init__(self, game_scene: GameScene) -> None:
        """Initialize the game map.

        Args:
            game_scene: The game scene.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.info("Initializing game map...")

        self.game_scene = game_scene

        initialize_worlds()
        initialize_tiles()

        self.viewport_size: tuple[int, int] = (
            game_scene.size[0] - game_scene.sidebar.SIDEBAR_SIZE[0],
            game_scene.size[1],
        )

        self.world: World | None = None

        self.surface = Surface(self.viewport_size)

        # NOTE: debug
        self.load_world("simulat.world.debug_world")

    def load_world(self, world_id: str) -> None:
        """Load a world.

        Args:
            world_id: The ID of the world to load.
        """
        self.logger.info(f"Loading world: {world_id}")

        self.world = get_world(world_id)

        # camera currently unused
        # self.camera: Camera = Camera(self.world, self.viewport_size)

    def input(self, *, events: list[pg.event.Event], keys: dict[int, bool]) -> None:
        """Handle input events.

        Args:
            key: The keys pressed.
        """

        if self.world is not None:
            # player movement
            if keys[pg.K_w]:
                self.world.player.velocity[1] += -1
            if keys[pg.K_s]:
                self.world.player.velocity[1] += 1
            if keys[pg.K_a]:
                self.world.player.velocity[0] += -1
            if keys[pg.K_d]:
                self.world.player.velocity[0] += 1

    def update(self, delta: float) -> None:
        """Update the game map.

        Args:
            delta: The time since the last frame.
        """
        if self.world is not None:
            self.world.player.update(delta)
            # self.camera.update(delta)
            try:
                standing_on_tile_name = self.world.player.current_tile.tile_type.label
            except KeyError:
                standing_on_tile_name = "Void"
            simulat.topbar.update_title(
                f"XY: {self.world.player.pos[0]:.3f}, {self.world.player.pos[1]:.3f} on "
                f"{standing_on_tile_name}"
            )

    def render(self) -> None:
        """Render the game map.

        This method renders the game map onto the surface. It fills the surface with a specific color,
        and then iterates over the chunks of the world to blit the tiles onto the surface based on the player's position.

        Returns:
            None
        """
        self.surface.fill((12, 34, 56))

        if self.world is not None:
            from src.simulat.core.scenes.game_scene.game_map.tiles.tile_type import (
                TILE_SIZE,
            )

            # calculate the number of chunks to render
            x_chunks = (
                math.ceil(self.viewport_size[0] / (self.world.CHUNK_SIZE * TILE_SIZE)) + 2  # fmt: skip
            )
            y_chunks = (
                math.ceil(self.viewport_size[1] / (self.world.CHUNK_SIZE * TILE_SIZE)) + 2  # fmt: skip
            )

            # render the chunks
            for y in range(y_chunks):
                for x in range(x_chunks):
                    # calculate the target chunk
                    target_x = (x - 1 + int(round((self.world.player.px_pos[0] - self.viewport_size[0] // 2) / (self.world.CHUNK_SIZE * TILE_SIZE))))  # fmt: skip
                    target_y = (y - 1 + int(round((self.world.player.px_pos[1] - self.viewport_size[1] // 2) / (self.world.CHUNK_SIZE * TILE_SIZE))))  # fmt: skip
                    target_chunk = (target_x, target_y)

                    # generate the target chunk if it doesn't exist
                    if target_chunk not in self.world.chunk_map:
                        self.world.chunk_map[target_chunk] = self.world.generate_chunk(
                            (target_x, target_y)
                        )

                    # render the tiles in the target chunk
                    for tile in self.world.chunk_map[target_chunk].values():
                        self.surface.blit(
                            tile.tile_type.texture,
                            (
                                tile.px_pos[0] - self.world.player.px_pos[0] + self.viewport_size[0] // 2,  # fmt: skip
                                tile.px_pos[1] - self.world.player.px_pos[1] + self.viewport_size[1] // 2,  # fmt: skip
                            ),
                        )

            # render the entities
            for entity in self.world.entities:
                entity.render(self.surface)

            # render the player
            self.world.player.render(self.surface)

        self.game_scene.surface.blit(self.surface.surface, (0, 0))
