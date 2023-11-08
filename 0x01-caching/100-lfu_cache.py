#!/usr/bin/python3
""" Python caching """
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Implement Least Frequently Used caching system
    """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """ Add items to cache
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
                else:
                    # discard the most recently used item
                    discarded = self.mru
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
                    self.cache_data[key] = item
                    self.mru = key
            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """ Get item by key
        """
        if key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
