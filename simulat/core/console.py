# -*- coding: utf-8 -*-
"""Console module for simulat."""

from __future__ import annotations

from typing import Any, Final

import pygame as pg

from simulat.core.colors import SimulatPalette
from simulat.core.game import simulat
from simulat.core.object import Object
from simulat.core.surfaces.surface import Surface


class Console(Object):
    """Console class.

    A developer console for debugging and testing.

    Usage:
    - Toggle the console by pressing the backquote key (`).
    - Type a command and press Enter to execute it.
    - Prefix a command with `!` to evaluate it (e.g. `!2 + 2`).
    """

    def __init__(self) -> None:
        """Initialize the console."""
        super().__init__()
        self.visible: bool = False
        self.counter: int = 0

        self.history: list[str] = []
        self.history_index: int = 0

        self.EVAL_GLOBALS: Final[dict[str, Any]] = {"simulat": simulat, "pg": pg}
        self.COMMAND_MAP: Final[dict[str, Any]] = {
            "help": "Available commands:\nexit, quit, toggle, help",
            "exit": self.toggle,
            "quit": self.toggle,
            "toggle": self.toggle,
        }

        self.command: str = ""
        self.result: str = ""
        self._result_changed: bool = False
        self.cursor: int = 0

        self.colors: dict[str, str] = {
            "border": SimulatPalette.ACCENT_PURPLE,
            "command": SimulatPalette.ACCENT_BLUISH_DISABLED,
            "result": SimulatPalette.BACKGROUND,
        }

        self.surface = Surface((simulat.INTERNAL_SCREEN_SIZE[0] - 100, 288), (50, 36))
        self.surface.fill(self.colors["border"])
        self.surface.surface.set_alpha(200)

        self.command_surface = Surface((self.surface.width - 2, 12), (1, 1))
        self.command_surface.fill(self.colors["command"])

        # self.result_surface = self.surface.subsurface((1, 13), (self.surface.width - 2, self.surface.height - 14))
        self.result_surface = Surface(
            (self.surface.width - 2, self.surface.height - 14), (1, 13)
        )
        self.result_surface.fill(self.colors["result"])

    def _execute(self, command: str) -> str:
        """Execute a command.

        Args:
            command (str): The command to execute.

        Returns:
            str: The result of the command.
        """
        # command map lookup
        if command in self.COMMAND_MAP:
            self.logger.debug(
                f"Command mapped ({command}): {repr(self.COMMAND_MAP[command])}"
            )
            if callable(self.COMMAND_MAP[command]):
                result = self.COMMAND_MAP[command]()
                return result if result is not None else "Command executed."
            return self.COMMAND_MAP[command]

        # if the command is not in the command map and doesn't start with `!`
        # (indicating an eval/exec command), return an error
        elif not command.startswith("!"):
            return "Command not found."

        # remove the `!` from the command
        command = command.lstrip("!")

        # eval/exec the command
        try:
            # eval
            try:
                result = str(eval(command, self.EVAL_GLOBALS))
            except SyntaxError:
                # exec
                exec(command, self.EVAL_GLOBALS)
                result = "Command executed."
        except Exception as e:
            result = f"An error occured:\n{str(e)}"
            self.logger.warning(f"Command error: {str(e)}")
        return result

    def _render_result(self, result: Any) -> None:
        """Render the result of the command.

        Args:
            result (Any): The result of the command.
        """
        self.result_surface.fill(self.colors["result"])
        self.result_surface.blit_text(str(result), (0, 0))
        self._result_changed = False

    def toggle(self) -> None:
        """Toggle the console."""
        self.visible = not self.visible
        if self.visible:
            # set key repeat
            pg.key.set_repeat(500, 50)
            # display a warning message
            self.result: str = (
                "WARNING: This is a developer console.\nDO NOT paste code from untrusted sources."
            )
            self._result_changed: bool = True
        else:
            # reset key repeat
            pg.key.set_repeat()
        self.logger.debug(f"Console toggled, visible: {self.visible}")

    def update(self) -> None:
        """Update the console."""
        if not self.visible:
            return

        self.counter += 1
        if self.counter > 60:
            self.counter = 0

        for event in self._input["events"]:
            if event.type == pg.KEYDOWN:
                # remove the character before the cursor
                if event.key == pg.K_BACKSPACE:
                    self.command = self.command[:self.cursor - 1] + self.command[self.cursor:]  # fmt: skip
                    self.cursor -= 1

                # remove the character after the cursor
                elif event.key == pg.K_DELETE:
                    self.command = self.command[: self.cursor] + self.command[self.cursor + 1:]  # fmt: skip

                # move the cursor left
                elif event.key == pg.K_LEFT:
                    self.cursor -= 1

                # move the cursor right
                elif event.key == pg.K_RIGHT:
                    self.cursor += 1

                # move the cursor to the beginning of the command
                elif event.key == pg.K_HOME:
                    self.cursor = 0

                # move the cursor to the end of the command
                elif event.key == pg.K_END:
                    self.cursor = len(self.command)

                # loop through the command history backwards
                elif event.key == pg.K_UP:
                    if self.history_index > 0:
                        self.history_index -= 1
                        self.command = self.history[self.history_index]
                        self.cursor = len(self.command)

                # loop through the command history forwards
                elif event.key == pg.K_DOWN:
                    if self.history_index < len(self.history) - 1:
                        self.history_index += 1
                        self.command = self.history[self.history_index]
                        self.cursor = len(self.command)

                # submit the command
                elif event.key == pg.K_RETURN:
                    self.history.append(self.command)
                    self.history_index = len(self.history)
                    self.logger.info(f"Command entered: {self.command}")
                    self.result = self._execute(self.command)
                    self._result_changed = True
                    self.command = ""
                    self.cursor = 0

                # ignore special keys
                elif event.key in [
                    pg.K_BACKQUOTE,
                    pg.K_LSHIFT,
                    pg.K_RSHIFT,
                    pg.K_LCTRL,
                    pg.K_RCTRL,
                    pg.K_LALT,
                    pg.K_RALT,
                    pg.K_LMETA,
                    pg.K_RMETA,
                    pg.K_LSUPER,
                    pg.K_RSUPER,
                    pg.K_MODE,
                    pg.K_HELP,
                    pg.K_PRINT,
                    pg.K_SYSREQ,
                    pg.K_BREAK,
                    pg.K_MENU,
                    pg.K_INSERT,
                    pg.K_CAPSLOCK,
                ]:
                    pass

                # add a character to the command
                elif event.unicode.isprintable():
                    self.command = self.command[:self.cursor] + event.unicode + self.command[self.cursor:]  # fmt: skip
                    self.cursor += 1

                else:
                    self.logger.debug(f"Unhandled key: {event.key}")

        self.cursor = max(0, min(self.cursor, len(self.command)))

    def render(self) -> None:
        """Render the console."""
        if not self.visible:
            return

        self.surface.fill(self.colors["border"])
        self.command_surface.fill(self.colors["command"])

        # cursor
        cursor_char = "|" if self.counter % 60 < 30 else "¦"

        # render the command
        command_with_cursor: str = (
            self.command[:self.cursor] + cursor_char + self.command[self.cursor:]  # fmt: skip
        )
        no_command_text = "Type a command..."

        self.command_surface.blit_text(
            command_with_cursor if self.command else no_command_text,
            (0, 0),
        )

        # render the result
        if self._result_changed:
            self._render_result(self.result)

        self.surface.blit(self.command_surface.surface, self.command_surface.pos)
        self.surface.blit(self.result_surface.surface, self.result_surface.pos)

        simulat.internal_screen.blit(self.surface.surface, self.surface.pos)
