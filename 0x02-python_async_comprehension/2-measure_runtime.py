#!/usr/bin/env python3
'''measure_runtime of coroutine'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime coroutine'''
    start: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end: float = time.time()
    return end - start
