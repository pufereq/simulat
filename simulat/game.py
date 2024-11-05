# -*- coding: utf-8 -*-
"""Game module for simulat."""

from __future__ import annotations

from puffkit import __version__, PkApp, PkScene

from simulat.config_handler import ConfigHandler


class Simulat(PkApp):
    """Main class for simulat."""

    def __init__(self) -> None:
        """Initialize the game."""
        self.config_handler = ConfigHandler()

        super().__init__(
            app_name="simulat",
            app_version=__version__,
            display_size=(
                self.config_handler.get("resolution")["width"],
                self.config_handler.get("resolution")["height"],
            ),
            display_arguments={},
            internal_screen_size=(640, 360),
            fps=self.config_handler.get("fps_limit"),
        )

    def init(self) -> None:
        # self.scenes = {}
        pass


def init() -> None:
    """Initialize the game."""
    # set up logging
    import logging as lg

    lg.basicConfig(
        format="%(asctime)s : %(levelname)-8s : %(threadName)s : %(filename)s:"
        "%(lineno)d : %(name)s :: %(message)s",
        level=lg.DEBUG,
    )
    global simulat
    simulat = Simulat()
    simulat.init()
