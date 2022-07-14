#!/usr/bin/env python3
''' Exercise: Redis basic '''

from re import S
from typing import Union
import uuid
import redis

class Cache:
    ''''A Redis-based cache'''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in the cache '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    # create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format

    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        ''' Get data from the cache '''
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        ''' Get data from the cache '''
        data = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        ''' Get data from the cache '''
        data = self._redis.get(key)
        return int(data)
