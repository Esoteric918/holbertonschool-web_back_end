#!/usr/bin/env python3
"""Most Recently Used Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used Caching"""

    def __init__(self):
        """Initialize MRU cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
            if len(self.cache_data) > self.MAX_ITEMS:
                key = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(key[0]))

    def get(self, key):
        """Get item from cache"""
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key)
