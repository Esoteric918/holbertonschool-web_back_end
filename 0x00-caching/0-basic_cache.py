#!/usr/bin/env python3

''' Basic cache implementation '''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
