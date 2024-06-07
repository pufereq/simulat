# -*- coding: utf-8 -*-
"""Camera character."""

from __future__ import annotations

from src.simulat.core.characters.character import Character


class Camera(Character):
    def __init__(
        self, game_map: GameMap, pos: tuple[float, float], size_px: tuple[float, float]
    ) -> None:
        super().__init__(game_map, pos, size_px, "px", can_collide=False)
        self.max_distance_from_player: float = 8  # tiles

        self.logger.debug(f"Camera size: {self.px_size} px")

    def _cap_position(self, pos_tiles: tuple[float, float]) -> None:
        """
        Cap the camera position to within the distance to player. Then call
        the parent method to cap the position to within the map size.
        """
        player_pos = self.game_map.player.pos
        pos_tiles = list(pos_tiles)

        # cap x
        if abs(player_pos[0] - pos_tiles[0]) > self.max_distance_from_player:
            if player_pos[0] > pos_tiles[0]:
                pos_tiles[0] = player_pos[0] - self.max_distance_from_player
            else:
                pos_tiles[0] = player_pos[0] + self.max_distance_from_player

        # cap y
        if abs(player_pos[1] - pos_tiles[1]) > self.max_distance_from_player:
            if player_pos[1] > pos_tiles[1]:
                pos_tiles[1] = player_pos[1] - self.max_distance_from_player
            else:
                pos_tiles[1] = player_pos[1] + self.max_distance_from_player

        return super()._cap_position(pos_tiles)
