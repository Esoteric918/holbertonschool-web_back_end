#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async'''

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
from typing import List


async def wait_n(n, max_delay) -> List[float]:
    '''return the list of all the delays (float values)'''
    delays: List = []
    for i in range(n):
        delay = asyncio.create_task(wait_random(max_delay))
        delays.append(delay)
    res_list: List = []
    for task in asyncio.as_completed(delays):
        res: float = await task
        res_list.append(res)
    return res_list
