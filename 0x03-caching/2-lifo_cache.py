#!/usr/bin/python3
"""
LIFO caching exercise
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    lifo cache eviction system
    """

    def __init__(self):
        """
        call parents
        """
        BaseCaching.__init__(self)
        self.order = []

    def put(self, key, item):
        """
        put a value in cache
        :param key: key
        :param item: value
        :return: None
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

            if len(self.order) > BaseCaching.MAX_ITEMS:
                last = self.order.pop(-2)
                self.cache_data.pop(last)
                print('DISCARD: {}'.format(last))

    def get(self, key):
        """
        get a value from cache
        :param key: key
        :return: value or None
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
