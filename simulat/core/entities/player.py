# -*- coding: utf-8 -*-
"""Player module."""

from __future__ import annotations

import logging as lg

from simulat.core.entities.entity import Entity
from simulat.core.scenes.game_scene.game_map.world import World
from simulat.core.surfaces.surface import Surface


class Player(Entity):
    """Player class.

    The player is the character controlled by the player.
    """

    def __init__(
        self,
        world: World,
        pos: tuple[float, float],
    ) -> None:
        """Initialize the player.

        Args:
            world (World): The world.
            pos (tuple[float, float]): The player's position in tiles.
        """

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.logger.debug("Initializing player...")
        super().__init__(world, pos, (1, 1), "tiles")

    def render(self, surface: Surface) -> None:
        """Render the player.

        The player is rendered at the center of the viewport.

        Args:
            surface (Surface): The surface to render the player on.
        """
        from simulat.core.game import simulat

        game_map = simulat.scenes["GameScene"].game_map
        surface.blit(
            self.sprite.surface,
            (
                (game_map.viewport_size[0] - self.px_size[0]) // 2,
                (game_map.viewport_size[1] - self.px_size[1]) // 2,
            ),
        )
