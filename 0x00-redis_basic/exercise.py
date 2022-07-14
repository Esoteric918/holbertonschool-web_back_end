#!/usr/bin/env python3
''' Exercise: Redis basic '''

from functools import wraps
from typing import Callable, Union
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    '''counts the number of time Cache is called'''

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, int]:
        '''wrapper to increment the number of calls'''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

def call_history(method: Callable) -> Callable:
    '''adds the call history to the cache'''

    @wraps(method)
    def wrapper(self, *args) -> Union[str, int]:
        '''wrapper to add the call history'''
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        op = method(self, *args)
        self._redis.rpush(f"{key}:outputs", op)
        return op

    return wrapper

# implement a replay function to display the history of calls of a particular function.
# Use keys generated in previous tasks to generate the following output:

def replay(method: Callable) -> Callable:
    '''replays the call history'''
    @wraps(method)
    def wrapper(self, *args) -> Union[str, int]:
        '''wrapper to replay the call history'''
        key = method.__qualname__
        inputs = self._redis.lrange(f"{key}:inputs", 0, -1)
        outputs = self._redis.lrange(f"{key}:outputs", 0, -1)
        for input, output in zip(inputs, outputs):
            print(f"{key}({input}) -> {output}")
        return method(self, *args)

    return wrapper
class Cache:
    ''''A Redis-based cache'''

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store data in the cache '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


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
