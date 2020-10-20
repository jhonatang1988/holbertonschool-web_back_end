#!/usr/bin/env python3
"""
converts element_length into annotated function
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    converts element_length into annotated function
    :param lst: an iterable
    :return: a list of tuples that has inside a tuple and an int
    """
    return [(i, len(i)) for i in lst]
