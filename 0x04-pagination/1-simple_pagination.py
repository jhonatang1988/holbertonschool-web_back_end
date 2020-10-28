#!/usr/bin/env python3
"""
simple pagination
"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get page based on required page size
        :param page: num of page
        :param page_size: size of the page
        :return: list of lists with results. Each list one result
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start: end]
