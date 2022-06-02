#!/usr/bin/env python3

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

def task_wait_random(max_delay: int) -> None:
    task = asyncio.create_task(wait_random(max_delay))
    return task
