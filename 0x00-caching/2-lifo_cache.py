#!/usr/bin/env python3
''' 2-lifo_cache.py: LIFO Cache '''
from base_caching import BaseCaching
from typing import OrderedDict

class LIFOCache(BaseCaching):
    '''Inherit from BaseCaching and implement the following methods:'''

    def __init__(self):
        ''' initialize cache '''
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        '''add item to cache'''
        if key is None or item is None:
            self.cache_data[key] = item

            if key not in self.cache_list:
                self.cache_list.append(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.cache_list.pop(self.MAX_ITEMS - 1)
                print("DISCARD: {}".format(discarded))
                del self.cache_data[discarded]

    def get(self, key):
        ''' get item from cache '''
        if key or key in self.cache_data:
            return self.cache_data.get(key)

