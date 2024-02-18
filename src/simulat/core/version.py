# -*- coding: utf-8 -*-
"""Version information."""

import logging as lg
from typing import Final


def _get_version() -> str:
    """Get the version from the VERSION file."""
    logger = lg.getLogger(__name__)
    try:
        with open("VERSION", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        logger.warning("VERSION file not found, using 'unknown'.")
        return "unknown"


VERSION: Final[str] = _get_version()
