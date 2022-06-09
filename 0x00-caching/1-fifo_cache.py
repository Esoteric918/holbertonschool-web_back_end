#!/usr/bin/env python3
''' FIRST IN FIRST OUT cache system '''
from typing import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFO cache implementation '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' put item in cache '''
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key, val = self.cache_data.popitem(last=False)
                print('DISCARD:{}'.format(key))

    def get(self, key):
        ''' get item from cache '''
        if key or key in self.cache_data:
            return self.cache_data.get(key)
