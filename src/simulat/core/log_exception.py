# -*- coding: utf-8 -*-
"""Error handler module for simulat."""

from __future__ import annotations
import logging as lg


def log_exception(exc_type, exc_value, exc_traceback):
    """Handle errors.

    Args:
        exc_type: Type of the exception.
        exc_value: The exception.
        exc_traceback: The traceback.
    """
    # set up logging
    logger = lg.getLogger(__name__)

    logger.critical(f"{exc_type.__name__}: {exc_value}",
                    exc_info=(exc_type, exc_value, exc_traceback))
