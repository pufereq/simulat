# -*- coding: utf-8 -*-

from __future__ import annotations

import logging as lg
from typing import Final

from src.simulat.core.scenes.game_scene.game_map.tiles.map_tile import MapTile


class World:
    """World class.

    The world is the environment in which the game takes place. It contains
    the layout of the map, the player, and other entities.
    """

    CHUNK_SIZE: Final[int] = 8  # tiles

    def __init__(
        self,
        _id: str,
        label: str,
        description: str,
        layout: list[list[str]],
        player_pos: tuple[float, float],
    ) -> None:
        """Initialize the world.

        Args:
            _id (str): The world's ID.
            label (str): The world's label.
            description (str): The world's description.
            layout (list[list[str]]): The layout of the map.
            player_pos (tuple[float, float]): The player's initial position in tiles.
        """
        from src.simulat.core.characters.player import Player

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.info("Initializing world...")

        self.id: str = _id
        self.label: str = label
        self.description: str = description
        self.layout: list[list[str]] = layout

        self.size: tuple[int, int] = (len(self.layout[0]), len(self.layout))
        self.chunk_map: dict[tuple[int, int], dict[tuple[int, int], MapTile]] = {}
        self.collidables: dict[tuple[int, int], MapTile] = {}

        self.player: Player = Player(self, player_pos)

        from src.simulat.core.characters.character import Character

        self.entities: list[Character] = []

        from src.simulat.core.scenes.game_scene.game_map.world_manager import add_world

        add_world(self)

    def generate_chunk(self, x: int, y: int) -> dict[tuple[int, int], MapTile]:
        """Generate a chunk of the world.

        Args:
            x (int): The x-coordinate of the chunk.
            y (int): The y-coordinate of the chunk.

        Returns:
            dict[tuple[int, int], MapTile]: The chunk data.
        """
        chunk_data: dict[tuple[int, int], MapTile] = {}
        for y_offset in range(self.CHUNK_SIZE):
            for x_offset in range(self.CHUNK_SIZE):
                # get the actual tile coordinates
                tile_x = x * self.CHUNK_SIZE + x_offset
                tile_y = y * self.CHUNK_SIZE + y_offset
                try:
                    # check if the tile is out of bounds to prevent
                    # the layout from being accessed with negative indices
                    if tile_x < 0 or tile_y < 0:
                        raise IndexError

                    # create a MapTile object for the tile
                    chunk_data[(x_offset, y_offset)] = MapTile(
                        (tile_x, tile_y), self.layout[tile_y][tile_x]
                    )

                    # check if the tile is collidable and add it to
                    # the collidables dictionary
                    if chunk_data[(x_offset, y_offset)].tile_type.collision:
                        self.collidables[(tile_x, tile_y)] = chunk_data[
                            (x_offset, y_offset)
                        ]
                except IndexError:
                    # for now, just ignore out of bounds tiles
                    # chunk_data[(x_offset, y_offset)] = MapTile(
                    #     (tile_x, tile_y), "simulat.tile.grass"
                    # )
                    pass
        return chunk_data
