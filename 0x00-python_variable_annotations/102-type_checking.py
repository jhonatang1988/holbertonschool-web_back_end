#!/usr/bin/env python3
"""
correct code to comply with mypy
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
"""
from typing import List, Any, Union


def zoom_array(lst: List[Any], factor: Union[int, float] = 2) -> List[Any]:
    """
    correct code to comply with mypy
    :param lst: list
    :param factor: factor
    :return: list or tuple
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
