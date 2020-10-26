#!/usr/bin/env python3
"""
basic dictionary
"""
from typing import Any

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    basic dictionary
    """

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key: str, item: Any):
        """
        add to the dict cache
        :param key: key
        :param item: value
        :return: None
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        get a value from key
        :param key: key
        :return: value or None
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
