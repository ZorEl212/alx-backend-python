#!/usr/bin/env python3
"""Make multiplixer"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
        return lambda x: x * multiplier
