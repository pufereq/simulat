# -*- coding: utf-8 -*-
"""Camera character."""

from __future__ import annotations

from src.simulat.core.characters.character import Character


class Camera(Character):
    def __init__(self, game_map: GameMap, pos: tuple[float, float]) -> None:
        super().__init__(game_map, pos, game_map.display_size, "px",
                         can_collide=False)
        self.logger.debug(f"Camera size: {self.px_size} px")
