#!/usr/bin/python3
"""
LFU caching exercise
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU cache eviction system
    """

    def __init__(self):
        """
        call parents
        """
        BaseCaching.__init__(self)
        self.order = []
        self.count = {}

    def organize_from_counter(self):
        """
        organize item per counter, not if counter in zero
        :return: None
        """
        for k, v in sorted(self.count.items(), key=lambda p: p[1]):
            if v > 0:
                self.order.remove(k)
                self.order.append(k)

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

            if key in self.count:
                self.count[key] += 1
            else:
                self.count[key] = 0

            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

            if len(self.order) > BaseCaching.MAX_ITEMS:
                last = self.order.pop(0)
                self.count.pop(last)
                self.cache_data.pop(last)

                print('DISCARD: {}'.format(last))

            self.organize_from_counter()

    def get(self, key):
        """
        get a value from cache
        :param key: key
        :return: value or None
        """
        if key in self.cache_data:
            self.count[key] += 1

            self.organize_from_counter()

            return self.cache_data[key]

        else:
            return None
