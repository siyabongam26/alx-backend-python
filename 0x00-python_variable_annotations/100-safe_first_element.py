#!/usr/bin/env python3
"""
This module provides a function to return the first element of a sequence, or None if the sequence is empty.
"""

from typing import Sequence, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists, otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Optional[Any]: The first element or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
