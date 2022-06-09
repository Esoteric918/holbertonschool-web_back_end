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
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = self.cache_data.popitem(last=False)
            print('DISCARD:{}'.format(key[0]))

    def get(self, key):
        ''' get item from cache '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
