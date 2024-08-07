# -*- coding: utf-8 -*-
"""Camera character."""

from __future__ import annotations

from simulat.core.entities.entity import Entity
from simulat.core.scenes.game_scene.game_map.world import World


class Camera(Entity):
    def __init__(self, world: World, size_px: tuple[float, float]) -> None:
        super().__init__(world, (0, 0), size_px, "px", can_collide=False)
        self.max_distance_from_player: float = 8  # tiles
        self.attached_to_player: bool | None = None
        self.world = world

        self.logger.debug(f"Camera size: {self.px_size} px")

    def _cap_position(self, pos_tiles: tuple[float, float]) -> None:
        """
        Cap the camera position to within the distance to player. Then call
        the parent method to cap the position to within the map size.
        """
        player_pos = self.world.player.pos
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
