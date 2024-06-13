# -*- coding: utf-8 -*-
"""World manager module for GameMap.

This module contains the world manager, which is responsible for managing the
worlds used in the game map.
"""

from __future__ import annotations

import logging as lg
from typing import Any

worlds: dict[str, Any] = {}


def initialize_worlds() -> None:
    """Initialize the worlds."""
    logger = lg.getLogger(f"{__name__}.{initialize_worlds.__name__}")

    logger.info("Initializing worlds...")
    from data.simulat.worlds.debug_world.debug_world import DebugWorld

    add_world(DebugWorld())


def add_world(world: Any) -> None:
    """Add a world to the world manager.

    Args:
        world: The world to add.
    """
    logger = lg.getLogger(f"{__name__}.{add_world.__name__}")
    worlds[world.id] = world
    logger.info(f"Added world {world.id}")


def get_world(world_id: str) -> Any:
    """Get a world by its ID.

    Args:
        world_id: The ID of the world to get.

    Returns:
        The world with of the specified ID.
    """
    logger = lg.getLogger(f"{__name__}.{get_world.__name__}")
    try:
        return worlds[world_id]
    except KeyError:
        logger.error(f"World {world_id} not found")
        return None
