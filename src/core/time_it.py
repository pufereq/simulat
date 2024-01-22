# -*- coding: utf-8 -*-
"""Timing decorator."""

from __future__ import annotations
from functools import wraps

import logging as lg
import time as t


def time_it(func):
    """Decorator to time a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrap the function."""
        start = t.perf_counter()
        result = func(*args, **kwargs)
        end = t.perf_counter()
        lg.debug(f"{func.__name__} took {end - start} seconds to run.")
        return result
    return wrapper
