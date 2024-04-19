#!/usr/bin/env python3
"""Create a tuple"""
from typing import Tuple

def to_kv(k: str, v: int | float) -> Tuple[str, int | float]:
        return tuple((k, v**2))
