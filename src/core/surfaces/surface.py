# -*- coding: utf-8 -*-
"""Surface module for simulat."""

from __future__ import annotations
from typing import overload

import pygame as pg


class Surface:
    def __init__(self, size: tuple[int, int], pos: tuple[int, int] = (0, 0),
                 *, flags: int = 0, depth: int = 32,
                 masks: tuple[int, int, int, int] | None = None):
        self.size = size
        self.width = size[0]
        self.height = size[1]

        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.surface = pg.Surface(size, flags, depth)

    def fill(self, color: tuple[int, int, int]):
        return self.surface.fill(color)

    def convert(self, surface: pg.Surface):
        return self.surface.convert(surface)

    def blit(self, source: pg.Surface, dest: tuple[int, int],
             area: tuple[int, int, int, int] | None = None,
             special_flags: int = 0):
        return self.surface.blit(source, dest, area, special_flags)
