# -*- coding: utf-8 -*-
"""Map layout module."""

from __future__ import annotations

from typing import Final

from src.simulat.core.surfaces.game_map.tiles.collider_tiles.collider_tile import \
    ColliderTile
from src.simulat.core.surfaces.game_map.tiles.decorative_tiles.decorative_tile import \
    DecorativeTile


class MapLayout:
    """Map layout class.

    The map layout class contains the layout of the game map. It is a 2D list
    of strings, where each string represents a tile type. The map layout is
    used to generate the game map.

    Character meanings:
    -

    Attributes:
        MAP_LAYOUT (Final): The map layout.
    """
    CHAR_TO_TILE: Final = {
        "w": ColliderTile,
        " ": DecorativeTile,
    }

    MAP_LAYOUT: Final[str] = """\
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
w              w                                                               w
w             w                                                                w
w       wwwwww                                                                 w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
w                                                                              w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
"""

    @staticmethod
    def get_map_layout() -> list[list[str]]:
        """Return the map layout as a 2D list of strings.

        Returns:
            list[list[str]]: The map layout.
        """
        return [list(row) for row in MapLayout.MAP_LAYOUT.split("\n") if row]

    @staticmethod
    def get_tile_char_at(x: int, y: int) -> str:
        """Return the char tile at the given coordinates.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            str: The tile char.
        """
        return MapLayout.get_map_layout()[y][x]

    @staticmethod
    def get_tile(x: int, y: int):
        """Return the tile at the given coordinates.

        Args:
            x (int): The x coordinate.
            y (int): The y coordinate.

        Returns:
            str: The tile.
        """
        y = round(y)
        x = round(x)
        return MapLayout.CHAR_TO_TILE[MapLayout.get_tile_char_at(x, y)]

    @staticmethod
    def get_tile_from_char(char: str):
        """Return the tile by char.

        Args:
            char (str): The tile char.

        Returns:
            The tile class.
        """
        return MapLayout.CHAR_TO_TILE[char]
