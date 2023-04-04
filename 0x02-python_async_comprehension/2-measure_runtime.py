#!/usr/bin/env python3
"""
from async_comprehension measure the amount of time used to execute
the async comprehension file four times. """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    """
    time used to execute async_comprehension four times in parallel
    using asyncio.gather
    """
    begin_time = time.perf_counter()
    my_lists = [asyncio.create_task(async_comprehension()) for i in range(4)]
    time_exc = await asyncio.gather(*my_lists)
    end_time = time.perf_counter()
    time_spent = time.perf_counter() - begin_time
    return time_spent
