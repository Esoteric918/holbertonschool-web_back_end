#!/usr/bin/env python3
'''coroutine async_generator'''

import asyncio
from typing import Generator, List
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    '''async_generator'''
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
