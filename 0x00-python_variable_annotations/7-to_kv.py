#!/usr/bin/env python3
"""Define function to_kv."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with string k and the square of int/float v."""
    return (k, v ** 2)
