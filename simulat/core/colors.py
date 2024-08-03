# -*- coding: utf-8 -*-
"""Color definitions."""

from typing import Final


def hex_to_rgba(hex_color: str) -> tuple[int, int, int, int]:
    """Convert a hex color to an RGBA tuple.

    Args:
        hex_color (str): Hex color string.

    Returns:
        tuple[int, int, int, int]: RGBA tuple.
    """
    hex_color = hex_color.lstrip("#").lower()
    if len(hex_color) == 3:  # #RGB -> (RRR, GGG, BBB, 255)
        rgba_value = (
            int(hex_color[0], 16) * 17,  # R
            int(hex_color[1], 16) * 17,  # G
            int(hex_color[2], 16) * 17,  # B
            255,  # A
        )
    elif len(hex_color) == 6:  # #RRGGBB -> (RRR, GGG, BBB, 255)
        rgba_value = (
            int(hex_color[:2], 16),  # R
            int(hex_color[2:4], 16),  # G
            int(hex_color[4:6], 16),  # B
            255,  # A
        )
    elif len(hex_color) == 8:  # #RRGGBBAA -> (RRR, GGG, BBB, AAA)
        rgba_value = (
            int(hex_color[:2], 16),  # R
            int(hex_color[2:4], 16),  # G
            int(hex_color[4:6], 16),  # B
            int(hex_color[6:8], 16),  # A
        )
    else:
        raise ValueError(f"Invalid hex color: {hex_color}")
    return rgba_value


class BasicPalette:
    """A class containing basic color definitions."""

    BLACK: Final[str] = "#000000"
    WHITE: Final[str] = "#ffffff"
    RED: Final[str] = "#ff0000"
    GREEN: Final[str] = "#00ff00"
    BLUE: Final[str] = "#0000ff"
    YELLOW: Final[str] = "#ffff00"
    CYAN: Final[str] = "#00ffff"
    MAGENTA: Final[str] = "#ff00ff"
    ORANGE: Final[str] = "#ff7f00"
    PURPLE: Final[str] = "#7f00ff"
    PINK: Final[str] = "#ff007f"
    BROWN: Final[str] = "#7f3f00"
    GREY: Final[str] = "#808080"
    LIGHT_GREY: Final[str] = "#d3d3d3"
    DARK_GREY: Final[str] = "#a9a9a9"


class SimulatPalette:
    """A class containing the simulat color palette."""

    BACKGROUND: Final[str] = "#364652"
    FOREGROUND: Final[str] = "#EDF2EF"
    ACCENT_PURPLE: Final[str] = "#9D8DF1"
    ACCENT_BLUISH: Final[str] = "#9CB7C7"
    ACCENT_BLUISH_DISABLED: Final[str] = "#7E898F"
    HIGHLIGHT: Final[str] = "#9AE19D"
    SHADOW: Final[str] = "#251A18"
