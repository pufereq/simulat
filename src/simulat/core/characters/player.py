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

    def render(self) -> None:
        from src.simulat.core.game import simulat
        simulat.topbar.update_title(
            f"XY: {self.pos[0]:.3f}, {self.pos[1]:.3f}"
        )
        return super().render()
