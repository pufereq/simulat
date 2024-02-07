# -*- coding: utf-8 -*-
"""Player module."""

from __future__ import annotations

import logging as lg

from src.simulat.core.characters.character import Character


class Player(Character):
    """Player class.

    The player is the character controlled by the user. It inherits from
    `Character`.
    """

    def __init__(self, game_map: GameMap, pos: tuple[float, float], ) -> None:
        """Initialize the player."""

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.debug("Initializing player...")
        super().__init__(game_map, pos)

    def _cap_position(self) -> None:
        """Cap the player's position to the game map's size."""

        self.rect.x = max(
            min(self.rect.x, self.game_map.width - self.rect.width),
            0
        )
        self.rect.y = max(
            min(self.rect.y, self.game_map.height - self.rect.height),
            0
        )

    def move(self, dx: int, dy: int) -> None:
        """Move the player.

        Args:
            dx (float): Horizontal distance to move (tiles).
            dy (float): Vertical distance to move (tiles).
        """
        new_x, new_y = self.rect.center

        # move horizontally
        if dx != 0:
            new_x += dx
            self.velocity[0] = 0

        # move vertically
        if dy != 0:
            new_y += dy
            self.velocity[1] = 0

        self.rect.center = (new_x, new_y)
        self._cap_position()
