#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """
        Adds an item in the cache.
        If key or item is None, this method should
        not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key.
        If key is None or if the key doesnt exist in
        self.cache_data, return None
        """
        return self.cache_data.get(key, None)
