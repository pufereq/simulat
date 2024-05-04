# -*- coding: utf-8 -*-
"""TODO"""

from __future__ import annotations

import logging as lg

import pygame as pg

from src.simulat.core.surfaces.buttons.button import Button
from src.simulat.core.surfaces.surface import Surface


class ButtonContainer:
    """Button container class.

    A button container is a container for buttons. It is used to group buttons
    together and handle their input and rendering.

    Usage:
    ```python
    button_container = ButtonContainer(
        parent_surface,
        [
            Button("Button 1", (100, 100), (100, 50)),
            Button("Button 2", (100, 200), (100, 50))
        ]
    )
    ```
    """
    def __init__(self, parent: Surface, buttons: list[Button]):
        """Initialize the button container."""
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.info("Initializing button container...")

        self.parent = parent
        self.buttons = buttons

    def __iter__(self):
        return iter(self.buttons)

    def __getitem__(self, index: int) -> Button:
        return self.buttons[index]

    def __len__(self) -> int:
        return len(self.buttons)

    def input(self, *, events: list[pg.event.Event], keys: dict[int, bool],
              mouse_pos: tuple[int, int],
              mouse_buttons: tuple[bool, bool, bool]) -> None:
        """Handle input events.

        Args:
            events (list[pg.event.Event]): List of pygame events.
            keys (dict[int, bool]): Dictionary of pressed keys.
            mouse_pos (tuple[int, int]): Position of the mouse.
            mouse_buttons (tuple[bool, bool, bool]): State of the mouse buttons.
        """

        mouse_pos = (
            mouse_pos[0] - self.parent.pos_x,
            mouse_pos[1] - self.parent.pos_y
        )

        for button in self.buttons:
            button.input(events=events, keys=keys, mouse_pos=mouse_pos,
                         mouse_buttons=mouse_buttons)

    def render(self) -> None:
        """Render the button container."""
        for button in self.buttons:
            button.render(self.parent)
