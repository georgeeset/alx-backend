#!/usr/bin/env pyhton3
"""Caching mechod"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implement LFU method of caching
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.usage_frequency = []

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        for i, usage in enumerate(self.usage_frequency):
            if usage[0] == mru_key:
                mru_freq = usage[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif usage[1] < self.usage_frequency[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.usage_frequency[pos][1] > mru_freq:
                break
            ins_pos = pos
        self.usage_frequency.pop(mru_pos)
        self.usage_frequency.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Add item to cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                item_key, _ = self.usage_frequency[-1]
                self.cache_data.pop(item_key)
                self.usage_frequency.pop()
                print("DISCARD:", item_key)
            self.cache_data[key] = item
            ins_index = len(self.usage_frequency)   
            for i, usage in enumerate(self.usage_frequency):
                if usage[1] == 0:
                    ins_index = i
                    break
            self.usage_frequency.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
