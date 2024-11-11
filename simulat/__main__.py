# -*- coding: utf-8 -*-

from __future__ import annotations


def main() -> None:
    """Main entry point of simulat."""
    from simulat.game import app_init

    app_init()

    from simulat.game import simulat

    simulat.run()


if __name__ == "__main__":
    main()
