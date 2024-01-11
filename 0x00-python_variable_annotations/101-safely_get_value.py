#!/usr/bin/env python3
"""Define function safely_get_value."""

from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value associated with the key
    in the dictionary or the default value."""
    if key in dct:

        return dct[key]

    else:

        return default
