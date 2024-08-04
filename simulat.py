#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simulat launcher."""

from simulat.core.game import init

if __name__ == "__main__":
    init()

    from simulat.core.game import simulat

    simulat.run()
