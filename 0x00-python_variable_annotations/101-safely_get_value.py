#!/usr/bin/env python3
"""
type variables for generic functions
"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    type variables for generic functions
    :param dct: a mapping of anything
    :param key: anything
    :param default: key or None
    :return: Anything or VT
    """
    if key in dct:
        return dct[key]
    else:
        return default
