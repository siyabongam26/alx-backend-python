#!/usr/bin/env python3
"""
This module provides a function to zoom into an array by a given factor.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on a tuple of integers by repeating each item in the tuple a given number of times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: A list containing the zoomed-in elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
