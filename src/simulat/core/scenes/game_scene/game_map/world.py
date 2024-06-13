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

    def generate_chunk(self, pos: tuple[int, int]) -> dict[tuple[int, int], MapTile]:
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
                tile_pos = (
                    pos[0] * self.CHUNK_SIZE + x_offset,
                    pos[1] * self.CHUNK_SIZE + y_offset,
                )
                try:
                    # check if the tile is out of bounds to prevent
                    # the layout from being accessed with negative indices
                    if tile_pos[0] < 0 or tile_pos[1] < 0:
                        raise IndexError

                    # create a MapTile object for the tile
                    chunk_data[(x_offset, y_offset)] = MapTile(
                        tile_pos, self.layout[tile_pos[1]][tile_pos[0]]
                    )

                    # check if the tile is collidable and add it to
                    # the collidables dictionary
                    if chunk_data[(x_offset, y_offset)].tile_type.collision:
                        self.collidables[tile_pos] = chunk_data[(x_offset, y_offset)]
                except IndexError:
                    # for now, just ignore out of bounds tiles
                    # chunk_data[(x_offset, y_offset)] = MapTile(
                    #     (tile_x, tile_y), "simulat.tile.grass"
                    # )
                    pass
        return chunk_data

    def get_tile(self, pos: tuple[int, int]) -> MapTile:
        """Get the tile at the specified coordinates.

        Args:
            pos (tuple[int, int]): The coordinates of the tile to get.

        Returns:
            MapTile: The tile at the specified coordinates.
        """
        chunk_pos = (pos[0] // self.CHUNK_SIZE, pos[1] // self.CHUNK_SIZE)
        chunk_offset = (pos[0] % self.CHUNK_SIZE, pos[1] % self.CHUNK_SIZE)
        try:
            return self.chunk_map[chunk_pos][chunk_offset]
        except KeyError:
            self.chunk_map[chunk_pos] = self.generate_chunk(chunk_pos)
            return self.chunk_map[chunk_pos][chunk_offset]
