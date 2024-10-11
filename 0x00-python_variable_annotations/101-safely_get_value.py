#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary. If the key is not found, it returns a default value.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to get the value.
        key (Any): The key to search for.
        default (Union[T, None], optional): The default value if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
