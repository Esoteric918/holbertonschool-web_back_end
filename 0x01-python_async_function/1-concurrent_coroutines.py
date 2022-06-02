#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async'''

wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n, max_delay) -> List[float]:
    '''return the list of all the delays (float values)'''
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return delays
