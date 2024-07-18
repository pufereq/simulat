# -*- coding: utf-8 -*-
"""Surface module for simulat."""

from __future__ import annotations

import logging as lg

import pygame as pg

from simulat.core.colors import SimulatPalette
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
        color: (
            tuple[int, int, int] | tuple[int, int, int, int] | str
        ) = SimulatPalette.FOREGROUND,
        font: str = "main",
        antialias: bool = True,
    ):
        """Add text to the surface.

        Args:
            text (str): Text to add.
            pos (tuple[int | str, int | str]): Position to add the text at.
                Can be a number or "left", "center" or "right" for horizontal
                align, and "top", "center" or "bottom" for vertical align.
            color (tuple[int, int, int]): Color of the text. (R, G, B)
            font (str, optional): Name of the font to use.
                Defaults to "main".
        """
        if pos[0] == "left":
            x_pos = 0
        elif pos[0] == "center":
            x_pos = (self.width - simulat.fonts[font].size(text)[0]) // 2
        elif pos[0] == "right":
            x_pos = self.width - simulat.fonts[font].size(text)[0]
        else:
            if isinstance(pos[0], str):
                raise ValueError(
                    f"Invalid horizontal position: {pos[0]}. Avaliable values:"
                    " number (int), 'left', 'center', 'right'"
                )
            x_pos = pos[0]

        if pos[1] == "top":
            y_pos = 0
        elif pos[1] == "center":
            y_pos = (self.height - simulat.fonts[font].size(text)[1]) // 2
        elif pos[1] == "bottom":
            y_pos = self.height - simulat.fonts[font].size(text)[1]
        else:
            if isinstance(pos[1], str):
                raise ValueError(
                    f"Invalid vertical position: {pos[1]}. Avaliable values:"
                    " number (int), 'top', 'center', 'bottom'"
                )
            y_pos = pos[1]

        if isinstance(color, str):
            color_str: str = color.strip("#").lower()

            if len(color_str) == 3:  # #RGB -> (RRR, GGG, BBB, 255)
                color = (
                    int(color_str[0], 16) * 17,  # R
                    int(color_str[1], 16) * 17,  # G
                    int(color_str[2], 16) * 17,  # B
                    255,  # A
                )
            elif len(color_str) == 6:  # #RRGGBB -> (RRR, GGG, BBB, 255)
                color = (
                    int(color_str[:2], 16),  # R
                    int(color_str[2:4], 16),  # G
                    int(color_str[4:6], 16),  # B
                    255,  # A
                )
            elif len(color_str) == 8:  # #RRGGBBAA -> (RRR, GGG, BBB, AAA)
                color = (
                    int(color_str[:2], 16),  # R
                    int(color_str[2:4], 16),  # G
                    int(color_str[4:6], 16),  # B
                    int(color_str[6:8], 16),  # A
                )

        text_surface = simulat.fonts[font].render(text, antialias, color)

        if text_surface.get_width() > self.width:
            self.logger.warning(
                f"Text too wide for surface: {text_surface.get_width()} >"
                f" {self.width}"
            )

        self.blit(text_surface, (x_pos, y_pos))


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
