# -*- coding: utf-8 -*-
"""Timing decorator."""

from __future__ import annotations

import logging as lg
import time as t
from functools import wraps


def time_it(func):
    """Decorator to time a function."""
    logger = lg.getLogger(f"{__name__}.{func.__name__}")

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrap the function."""
        start = t.perf_counter()
        result = func(*args, **kwargs)
        end = t.perf_counter()
        logger.debug(f"{func.__name__} took {end - start} seconds to run.")
        return result

    return wrapper


class Timer:
    """Timer context class.

    Usage:
    ```python
    with Timer() as t:
        # do something
    print(t.elapsed)
    ```
    """

    def __init__(self) -> None:
        """Initialize the timer."""
        pass

    def __enter__(self) -> Timer:
        """Enter the context."""
        self.start = t.perf_counter()
        return self

    def __exit__(self, *args):
        """Exit the context."""
        self.end = t.perf_counter()
        self.elapsed = self.end - self.start
