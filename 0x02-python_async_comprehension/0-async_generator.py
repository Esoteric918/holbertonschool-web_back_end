#!/usr/bin/env python3
'''coroutine async_generator'''

import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    '''async_generator'''
    result = []
    for i in range(10):
        result.append(uniform(0, 10))
        yield result[-1]
        await asyncio.sleep(1)
