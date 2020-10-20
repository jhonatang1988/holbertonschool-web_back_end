#!/usr/bin/env python3
"""
square values
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    square values
    :param k: str
    :param v: int or float
    :return: tuple with key and square the value
    """
    return k, float(v ** 2)
