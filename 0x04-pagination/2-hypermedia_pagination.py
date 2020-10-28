#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


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
        start: int
        end: int
        start, end = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) \
            -> Dict[str, Union[int, List[list], None, float]]:
        """
        get hypermedia pagination
        :param page: num of page
        :param page_size: size of page
        :return:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset_page = self.get_page(page, page_size)
        real_page_size = len(dataset_page)
        is_next_page = self.get_page(page + 1, page_size)
        if is_next_page:
            next_page_num = page + 1
        else:
            next_page_num = None
        try:
            is_previous_page = self.get_page(page - 1, page_size)
            if is_previous_page:
                previous_page_num = page - 1
            else:
                previous_page_num = None
        except AssertionError:
            previous_page_num = None

        total_pages: float = len(self.dataset()) / float(page_size)

        if total_pages.is_integer():
            total_pages_int = int(total_pages)
        else:
            total_pages_int = math.floor(total_pages) + 1
        return {
            'page_size': real_page_size,
            'page': page,
            'data': dataset_page,
            'next_page': next_page_num,
            'prev_page': previous_page_num,
            'total_pages': total_pages_int
        }
