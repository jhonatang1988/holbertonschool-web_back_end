#!/usr/bin/env python3
"""
sums a list of floats
"""
import functools
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sums a list of floats
    :param input_list: list of floats
    :return: sum of floats
    """
    return functools.reduce(lambda a, b: a + b, input_list)
