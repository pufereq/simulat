# -*- coding: utf-8 -*-
"""Surface module for simulat."""

from __future__ import annotations
from typing import overload

import pygame as pg

from ..game import simulat


class Surface:
    """Base class for surfaces.

    A surface is a part of the screen. It can be a scene, a topbar, a button,
    etc. Each surface has its own class, which inherits from this class.
    """
    def __init__(self, size: tuple[int, int], pos: tuple[int, int] = (0, 0),
                 *, flags: int = 0, depth: int = 32,
                 masks: tuple[int, int, int, int] | None = None):
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
        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.surface = pg.Surface(size, flags, depth)

    def subsurface(self, size: tuple[int, int],
                   pos: tuple[int, int]) -> SubSurface:
        """Create a subsurface.

        Args:
            size (tuple[int, int]): Size of the subsurface.
            pos (tuple[int, int]): Position of the subsurface.

        Returns:
            SubSurface: The created subsurface.
        """
        return SubSurface(self, size, pos)

    def fill(self, color: tuple[int, int, int]):
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

    def blit(self, source: pg.Surface, dest: tuple[int, int],
             area: tuple[int, int, int, int] | None = None,
             special_flags: int = 0):
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

    def add_text(self, text: str, pos: tuple[int, int],
                 color: tuple[int, int, int],
                 font: pg.font.Font = simulat.fonts["main"]):
        """Add text to the surface.

        Args:
            text (str): Text to add.
            pos (tuple[int, int]): Position to add the text at.
            color (tuple[int, int, int]): Color of the text. (R, G, B)
            font (pg.font.Font, optional): Font to use. Defaults to
                simulat.fonts["main"].
        """
        text_surface = font.render(text, True, color)
        self.blit(text_surface, pos)


class SubSurface(Surface):
    """Base class for subsurfaces.

    A subsurface is a surface that is part of another surface. It can be a
    button, a text box, etc.
    """
    def __init__(self, parent: Surface, pos: tuple[int, int],
                 size: tuple[int, int] = (0, 0)):
        """Initialize the subsurface.

        Args:
            parent (Surface): Parent surface.
            pos (tuple[int, int]): Position of the subsurface.
            size (tuple[int, int], optional): Size of the subsurface.
                Defaults to (0, 0).
        """
        self.parent = parent
        self.parent_surface = parent.surface

        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.surface = self.parent_surface.subsurface(pos, size)
