#!/usr/bin/env python3
"""FIRST IN FIRST OUT CACHE"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' inherited methods '''

    def __init__(self):
        ''' init method '''
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' put method item in cache '''
        if (key and item):
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(key[0]))

    def get(self, key):
        ''' Get method to return value at key '''
        if key or key not in self.cache_data:
            return self.cache_data.get(key)
