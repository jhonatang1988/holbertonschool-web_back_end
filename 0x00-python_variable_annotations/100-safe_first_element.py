#!/usr/bin/env python3
"""
augment the code below with duck-typed annotations
The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    augment the code below with duck-typed annotations
    :param lst: list of anything
    :return: anything or None
    """
    if lst:
        return lst[0]
    else:
        return None
