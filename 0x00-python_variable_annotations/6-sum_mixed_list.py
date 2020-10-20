#!/usr/bin/env python3
"""
sums floats and integers
"""
import functools
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sums floats and integers
    :param mxd_lst: list of floats and ints
    :return: sums as a float
    """
    return float(functools.reduce(lambda a, b: a + b, mxd_lst))
