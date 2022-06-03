#!/usr/bin/env python3
'''an asychronous coroutine'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''wait for a random number of seconds between 0 and max_delay'''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
