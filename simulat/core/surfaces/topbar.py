# -*- coding: utf-8 -*-
"""Topbar module for simulat."""

from __future__ import annotations

import logging as lg

from simulat.core.colors import SimulatPalette
from simulat.core.surfaces.surface import Surface


class Topbar(Surface):
    def __init__(self):
        from ..game import simulat

        self.logger = lg.getLogger(f"{__name__}.{type(self).__name__}")
        self.logger.debug("Initializing topbar...")

        super().__init__((simulat.INTERNAL_SCREEN_SIZE[0], 12), (0, 0))

        self.debug_text: str = ""
        self.title_text: str = ""
        self.details_text: str = ""

        self.debug_color: list[str] = [
            SimulatPalette.FOREGROUND,
            SimulatPalette.BACKGROUND,
        ]
        self.title_color: list[str] = [
            SimulatPalette.FOREGROUND,
            SimulatPalette.BACKGROUND,
        ]
        self.details_color: list[str] = [
            SimulatPalette.FOREGROUND,
            SimulatPalette.BACKGROUND,
        ]

        # init sub-surfaces
        self._init_sub_surfaces()

        # add text
        self.update_debug("simulat")
        self.update_title("simulat")
        self.update_details("simulat")

    def _init_sub_surfaces(self):
        self.debug_surface = self.subsurface(
            (0, 0), (round(self.width * 0.3), self.height)
        )
        self.title_surface = self.subsurface(
            (round(self.width * 0.3), 0), (round(self.width * 0.4), self.height)
        )
        self.details_surface = self.subsurface(
            (round(self.width * 0.7), 0), (round(self.width * 0.3), self.height)
        )

        self.debug_surface.fill(self.debug_color[1])
        self.title_surface.fill(self.title_color[1])
        self.details_surface.fill(self.details_color[1])

    def update_debug(self, text: str):
        self.debug_text = text

        self.debug_surface.fill(self.debug_color[1])
        self.debug_surface.blit_text(
            self.debug_text,
            ("left", "center"),
            color=self.debug_color[0],
            font="topbar",
        )

    def update_title(self, text: str):
        self.title_text = text

        self.title_surface.fill(self.title_color[1])
        self.title_surface.blit_text(
            self.title_text,
            ("center", "center"),
            color=self.title_color[0],
            font="topbar",
        )

    def update_details(self, text: str):
        self.details_text = text

        self.details_surface.fill(self.details_color[1])
        self.details_surface.blit_text(
            self.details_text,
            ("right", "center"),
            color=self.details_color[0],
            font="topbar",
        )
