#!/usr/bin/env python3
"""
helper function to return indexes for particular page
"""


def index_range(page: int, page_size: int):
    """
    helper function to return indexes for particular page
    :param page: num page
    :param page_size: size of results
    :return: tuple with a range of indexes
    """
    last_index: int = page_size * page
    first_index: int = last_index - page_size

    return first_index, last_index
