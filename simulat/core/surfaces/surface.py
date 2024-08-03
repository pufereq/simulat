# -*- coding: utf-8 -*-
"""Surface module for simulat."""

from __future__ import annotations

import logging as lg

import pygame as pg

from simulat.core.colors import SimulatPalette, hex_to_rgba
from simulat.core.game import simulat


class Surface:
    """Base class for surfaces.

    A surface is a part of the screen. It can be a scene, a topbar, a button,
    etc. Each surface has its own class, which inherits from this class.
    """

    def __init__(
        self,
        size: tuple[int, int],
        pos: tuple[int, int] = (0, 0),
        *,
        flags: int = 0,
        depth: int = 24,
        masks: tuple[int, int, int, int] | None = None,
    ):
        """Initialize the surface.

        Args:
            size (tuple[int, int]): Size of the surface.
            pos (tuple[int, int], optional): Position of the surface.
            flags (int, optional): Flags for the surface. Defaults to 0.
            depth (int, optional): Color depth of the surface (bits).
                Defaults to 32.
            masks (tuple[int, int, int, int] | None, optional): Color masks for
                the surface. Defaults to None.
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.surface = pg.Surface(size, flags, depth)

    def input(
        self,
        *,
        events: list[pg.event.Event],
        keys: dict[int, bool],
        mouse_pos: tuple[int, int],
        mouse_buttons: tuple[bool, bool, bool],
    ) -> None:
        pass

    def subsurface(self, pos: tuple[int, int], size: tuple[int, int]) -> SubSurface:
        """Create a subsurface.

        Args:
            pos (tuple[int, int]): Position of the subsurface.
            size (tuple[int, int]): Size of the subsurface.

        Returns:
            SubSurface: The created subsurface.
        """
        return SubSurface(self, pos, size)

    def fill(
        self, color: tuple[int, int, int] | tuple[int, int, int, int] | str
    ) -> pg.Rect:
        """Fill the surface with a color.

        Args:
            color (tuple[int, int, int]): Color to fill the surface with.

        Returns:
            Rect: The area that was filled.
        """
        return self.surface.fill(color)

    def convert(self, surface: pg.Surface):
        """Convert the surface to the same pixel format as another surface.

        Args:
            surface (pg.Surface): Surface to convert to.

        Returns:
            Surface: The converted surface.
        """
        return self.surface.convert(surface)

    def blit(
        self,
        source: pg.Surface,
        dest: tuple[int, int],
        area: tuple[int, int, int, int] | pg.Rect | None = None,
        special_flags: int = 0,
    ):
        """Draw one surface onto another.

        Args:
            source (pg.Surface): Surface to draw.
            dest (tuple[int, int]): Position to draw the surface at.
            area (tuple[int, int, int, int] | None, optional): Area of the
                source surface to draw. Defaults to None.
            special_flags (int, optional): Special flags for the blit.
                Defaults to 0.

        Returns:
            Rect: The area that was drawn.
        """
        return self.surface.blit(source, dest, area, special_flags)

    def blit_text(
        self,
        text: str,
        pos: tuple[int | str, int | str],
        *,
        max_width: int | None = None,
        text_align: str = "left",
        vertical_align: str = "top",
        tab_size: int = 4,
        color: (
            tuple[int, int, int] | tuple[int, int, int, int] | str
        ) = SimulatPalette.FOREGROUND,
        bg_color: tuple[int, int, int] | tuple[int, int, int, int] | str | None = None,
        font: str = "main",
        antialias: bool = False,
    ):
        """Add text to the surface.

        Args:
            text (str): Text to add.
            pos (tuple[int | str, int | str]): Position of the text.
                Can be a number (int) or "left", "center", "right" for horizontal
                position and "top", "center", "bottom" for vertical position.
            max_width (int | None, optional): Maximum width of the text
                before wrapping. `0` means no wrapping. Defaults to None
                (surface width).
            text_align (str, optional): Horizontal alignment of the text.
                Avaliable values: "left", "center", "right". Defaults to "left".
            vertical_align (str, optional): Vertical alignment of the text.
                Avaliable values: "top", "middle", "bottom". Defaults to "top".
            color (tuple[int, int, int] | tuple[int, int, int, int] | str,
                optional): Color of the text. Defaults to SimulatPalette.FOREGROUND.
            bg_color (tuple[int, int, int] | tuple[int, int, int, int] | str | None,
                optional): Background color of the text. Defaults to None (transparent).
            font (str, optional): Name of the font to use.
                Defaults to "main".
            antialias (bool, optional): Whether to use font antialiasing.
                Defaults to False.
        """
        # color conversion
        if isinstance(color, str):
            color = hex_to_rgba(color)
        if isinstance(bg_color, str):
            bg_color = hex_to_rgba(bg_color)

        # position conversion
        if isinstance(pos[0], str):
            if pos[0] == "center":
                x_pos = self.width // 2
            elif pos[0] == "right":
                x_pos = self.width
            else:  # left
                x_pos = 0
        else:
            x_pos = pos[0]

        if isinstance(pos[1], str):
            if pos[1] == "center":
                y_pos = self.height // 2
            elif pos[1] == "bottom":
                y_pos = self.height
            else:
                y_pos = 0
        else:
            y_pos = pos[1]

        max_width = max_width if max_width is not None else self.width - x_pos

        # text preparation
        text = text.replace("\t", " " * tab_size)

        align_map = {
            "left": pg.FONT_LEFT,
            "center": pg.FONT_CENTER,
            "right": pg.FONT_RIGHT,
        }

        simulat.fonts[font].align = align_map[text_align]

        text_surface = simulat.fonts[font].render(
            text, antialias, color, bg_color, max_width
        )

        # vertical alignment
        if vertical_align == "middle":
            y_pos = self.height // 2 - text_surface.get_height() // 2
        elif vertical_align == "bottom":
            y_pos = self.height - text_surface.get_height()

        self.blit(text_surface, (x_pos, y_pos))

        # reset alignment
        simulat.fonts[font].align = pg.FONT_LEFT


class SubSurface(Surface):
    """Base class for subsurfaces.

    A subsurface is a surface that is part of another surface. It can be a
    button, a text box, etc.
    """

    def __init__(
        self, parent: Surface, pos: tuple[int, int], size: tuple[int, int] = (0, 0)
    ):
        """Initialize the subsurface.

        Args:
            parent (Surface): Parent surface.
            pos (tuple[int, int]): Position of the subsurface.
            size (tuple[int, int], optional): Size of the subsurface.
                Defaults to (0, 0).
        """
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")

        self.parent = parent
        self.parent_surface = parent.surface

        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.surface = self.parent_surface.subsurface(pos, size)
