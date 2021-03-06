#!/usr/bin/env python3
'''LRU Cache system implementation'''

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''Inherit from BaseCaching and implement the following methods:'''

    def __init__(self):
        ''' initialize LRU cache system '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''add item to cache assign to the dictionary key'''
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                key = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(key[0]))

    def get(self, key):
        ''' get item from cache '''
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
