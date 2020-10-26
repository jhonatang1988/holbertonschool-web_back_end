#!/usr/bin/python3
"""
FIFO caching exercise
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    fifo cache eviction system
    """

    def __init__(self):
        """
        call parents
        """
        super().__init__()
        self.order = []

    # def put(self, key, item):
    #     """
    #     put a value in cache
    #     :param key: key
    #     :param item: value
    #     :return: None
    #     """
    #     if key is None or item is None:
    #         pass
    #     else:
    #         self.cache_data[key] = item
    #
    #         if key in self.order:
    #             self.order.remove(key)
    #         self.order.append(key)
    #
    #         if len(self.order) > BaseCaching.MAX_ITEMS:
    #             last = self.order.pop(0)
    #             self.cache_data.pop(last)
    #             print(f'DISCARD: {last}')
    #             # self.cache_data.pop()
    #             # print(f'DISCARD:')

    def put(self, key, item):
        """
            modify cache data

            Args:
                key: of the dict
                item: value of the key
        """
        if key or item is not None:
            valuecache = self.get(key)
            if valuecache is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())[0]
                    del self.cache_data[keydel]
                    print("DISCARD: {}".format(keydel))

            self.cache_data[key] = item

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
