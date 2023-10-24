#!/usr/bin/env python3
"""
First-In First-Out caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
     inherits from BaseCaching and is a caching system:
     Implements First in first out principle
    """
    def __init__(self):
        """
        Initializes the cache
        """
        super().__init__()
        # make it a dictionary that remembers insersion order
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item in the cache
        If key or item is None, this method should
        not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Retrieves an item by key.
        If key is None or if the key doesnt exist in
        self.cache_data, return None
        """
        return self.cache_data.get(key, None)
