# -*- coding: utf-8 -*-

from __future__ import annotations

from simulat.core.game import init


def main() -> None:
    """Main entry point of simulat."""
    init()
    from simulat.core.game import simulat

    simulat.run()


if __name__ == "__main__":
    main()
