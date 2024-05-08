# -*- coding: utf-8 -*-
"""Button module."""

from __future__ import annotations

import logging as lg
from typing import Callable, Final

import pygame as pg

from src.simulat.core.game import simulat
from src.simulat.core.surfaces.surface import Surface
from src.simulat.core.colors import BasicPalette, SimulatPalette


class Button(Surface):
    """Button class.

    A button is a clickable surface that can be used to trigger an action.
    """
    def __init__(self, text: str, pos: tuple[int, int], size: tuple[int, int],
                 on_click: Callable[[], None] | None, *, enabled: bool = True,
                 font: str = "button") -> None:
        """Initialize the button.

        Args:
            text (str): Text displayed on the button.
            pos (tuple[int, int]): Position of the button.
            size (tuple[int, int]): Size of the button.
            on_click (Callable[[], None] | None): Function to call when the
                button is clicked.
            enabled (bool, optional): Whether the button is enabled. Defaults
                to True.
            font (str, optional): Font to use for the button text. Defaults to
                "main".
        """
        super().__init__(size, pos)
        self.pos = pos
        self.rect = pg.Rect(self.pos, size)

        self.logger.debug(f"Creating button: '{text}' at {pos}"
                          f" size: {size}, enabled: {enabled},"
                          f" action: {on_click}")

        self.enabled = enabled
        self.text = text

        # disabled, normal, hover, click
        self.state = "normal" if self.enabled else "disabled"

        # state: (bg, fg)
        self.color_scheme: Final[dict[str, tuple[str, str]]] = {
            "disabled": (SimulatPalette.ACCENT_BLUISH_DISABLED,
                         SimulatPalette.BACKGROUND),

            "normal": (SimulatPalette.ACCENT_BLUISH,
                       SimulatPalette.BACKGROUND),

            "hover": (SimulatPalette.HIGHLIGHT,
                      SimulatPalette.BACKGROUND),

            "click": (SimulatPalette.ACCENT_PURPLE,
                      SimulatPalette.FOREGROUND)
        }

        self.font = font
        self.on_click = on_click if on_click else None

        # create rounded corner overlay
        self.rounded_corner_overlay = Surface(size, pos)
        self.rounded_corner_overlay.surface.set_colorkey(BasicPalette.MAGENTA)
        self.rounded_corner_overlay.fill(SimulatPalette.BACKGROUND)
        pg.draw.rect(
            self.rounded_corner_overlay.surface,
            BasicPalette.MAGENTA,
            (0, 0, *size),
            border_radius=4
        )

    def __repr__(self) -> str:
        """Return a string representation of the button."""
        return f"Button({self.text}, {self.pos}, {self.size}, {self.on_click})"

    def input(self, *, events: list[pg.event.Event], keys: dict[int, bool],
              mouse_pos: tuple[int, int],
              mouse_buttons: tuple[bool, bool, bool]) -> None:
        """Handle input events.

        Args:
            events (list[pg.event.Event]): List of pygame events.
            keys (dict[int, bool]): Dictionary of pressed keys.
            mouse_pos (tuple[int, int]): Position of the mouse.
            mouse_buttons (tuple[bool, bool, bool]): State of the mouse
                buttons.
        """

        # if the button is disabled, set the state to "disabled" and return
        if not self.enabled:
            self.state = "disabled"
            return

        if self.rect.collidepoint(mouse_pos):
            if mouse_buttons[0]:  # left mouse button clicked
                self.state = "click"
            else:  # mouse over only
                self.state = "hover"
        else:  # normal state
            self.state = "normal"

        # handle button click, i hate this indentation
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if self.rect.collidepoint(mouse_pos):
                    self.logger.debug(f"Button {self.text} clicked.")
                    # call the on_click function if it exists
                    self.on_click() if self.on_click else None

    def render(self, parent: Surface) -> None:
        """Render the button.

        Args:
            parent (Surface): Parent surface to render the button on.
        """
        # fill the button with the correct color
        self.surface.fill(self.color_scheme[self.state][0])

        self.surface.blit(self.rounded_corner_overlay.surface, (0, 0))

        self.add_text(self.text, ("center", "center"),
                      color=self.color_scheme[self.state][1], font=self.font)

        parent.blit(self.surface, self.pos)
