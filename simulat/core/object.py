# -*- coding: utf-8 -*-
"""Object module for Simulat Framework."""

from __future__ import annotations

import logging as lg
from typing import Any


class Object:
    """Object class.

    Base class for all objects in simulat.
    """

    def __init__(self) -> None:
        """Initialize the object."""
        self.class_name: str = type(self).__name__
        self.full_class_name: str = f"{__name__}.{self.class_name}"
        self.logger = lg.getLogger(self.full_class_name)
        self.logger.debug(f"Initializing object {self.class_name}...")

        self._input: dict[str, Any] = {
            "events": [],
            "keys": {},
            "mouse_pos": (0, 0),
            "mouse_buttons": (False, False, False),
        }

    def input(
        self,
        events: list[Any],
        keys: dict[str, bool],
        mouse_pos: tuple[int, int],
        mouse_buttons: tuple[bool, bool, bool],
    ) -> None:
        """Update the input for the object."""
        self._input = {
            "events": events,
            "keys": keys,
            "mouse_pos": mouse_pos,
            "mouse_buttons": mouse_buttons,
        }

    def update(self) -> None:
        """Update the object."""
        self.logger.warning(
            f"update method not implemented for {self.full_class_name}."
        )
        raise NotImplementedError(f"{self.class_name}.update() method not implemented.")

    def render(self) -> None:
        """Render the object."""
        self.logger.warning(
            f"render method not implemented for {self.full_class_name}."
        )
        raise NotImplementedError(f"{self.class_name}.render() method not implemented.")

    def __str__(self) -> str:
        self.logger.warning(
            f"__str__ method not implemented for {self.full_class_name}."
        )
        return super().__str__()

    def __repr__(self) -> str:
        self.logger.warning(
            f"__repr__ method not implemented for {self.full_class_name}."
        )
        return super().__repr__()
