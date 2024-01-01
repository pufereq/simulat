#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simulat launcher."""

from src.core.game import init

if __name__ == "__main__":
    init()

    from src.core.game import simulat
    simulat.run()
