# -*- coding: utf-8 -*-
"""Topbar module for simulat."""

from __future__ import annotations

import logging as lg

from src.core.surfaces.surface import Surface


class Topbar(Surface):
    def __init__(self):
        from ..game import simulat
        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.debug("Initializing topbar...")

        super().__init__((simulat.SIZE[0], 24), (0, 0))

        # init sub-surfaces
        self._init_sub_surfaces()

        self.debug_text: str = ""
        self.title_text: str = ""
        self.details_text: str = ""

        # add text
        self.update_debug("simulat")
        self.update_title("simulat")
        self.update_details("simulat")

    def _init_sub_surfaces(self):
        self.debug_surface = self.subsurface(
            (0, 0),
            (round(self.width * 0.3), self.height)
        )
        self.title_surface = self.subsurface(
            (round(self.width * 0.3), 0),
            (round(self.width * 0.4), self.height)
        )
        self.details_surface = self.subsurface(
            (round(self.width * 0.7), 0),
            (round(self.width * 0.3), self.height)
        )

        self.debug_surface.fill((255, 0, 0))
        self.title_surface.fill((0, 255, 0))
        self.details_surface.fill((0, 0, 255))

    def update_debug(self, text: str):
        self.debug_text = text

        self.debug_surface.fill((255, 0, 0))
        self.debug_surface.add_text(
            self.debug_text, ("left", "center"),
            (255, 255, 255),
            "topbar"
        )

    def update_title(self, text: str):
        self.title_text = text

        self.title_surface.fill((0, 255, 0))
        self.title_surface.add_text(
            self.title_text, ("center", "center"),
            (255, 255, 255),
            "topbar"
        )

    def update_details(self, text: str):
        self.details_text = text

        self.details_surface.fill((0, 0, 255))
        self.details_surface.add_text(
            self.details_text, ("right", "center"),
            (255, 255, 255),
            "topbar"
        )
