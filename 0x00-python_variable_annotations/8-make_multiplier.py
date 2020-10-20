#!/usr/bin/env python3
"""
functions that returns another function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    functions that returns another function
    :param multiplier: float to multiply
    :return:
    """

    def fun(n: float) -> float:
        return n * multiplier

    return fun
