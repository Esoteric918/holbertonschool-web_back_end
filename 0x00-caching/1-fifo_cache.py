#!/usr/bin/env python3

from typing import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    ''' FIFO cache implementation '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
    def put(self, key, item):
        ''' put item in cache '''
        if key is None or item is None:
            return None
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = self.cache_data.popitem(last=False)
            print('DISCARD:', key[0])
    def get(self, key):
        ''' get item from cache '''
        if key is None:
            return None
        return self.cache_data.get(key)
