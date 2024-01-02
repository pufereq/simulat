# -*- coding: utf-8 -*-
"""Topbar module for simulat."""

from __future__ import annotations
import logging as lg

from .surface import Surface


class Topbar(Surface):
    def __init__(self):
        from ..game import SIZE
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.debug("Initializing topbar...")

        super().__init__((SIZE[0], 24), (0, 0))

        # init sub-surfaces
        self._init_sub_surfaces()

    def _init_sub_surfaces(self):
        self.debug_surface = self.subsurface(
            (0, 0),
            (self.width * 0.3, self.height)
        )
        self.title_surface = self.subsurface(
            (self.width * 0.3, 0),
            (self.width * 0.4, self.height)
        )
        self.details_surface = self.subsurface(
            (self.width * 0.7, 0),
            (self.width * 0.3, self.height)
        )

        self.debug_surface.fill((255, 0, 0))
        self.title_surface.fill((0, 255, 0))
        self.details_surface.fill((0, 0, 255))

