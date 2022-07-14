#!/usr/bin/env python3
''' Exercise: Redis basic '''

import uuid
import redis

class Cache:
    ''''A Redis-based cache'''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> any:
        ''' Store data in the cache '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    # create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format

    def get(key: str ):
        pass
