#!/usr/bin/env python3
"""
using the async_generator from the previous task, coroutine takes no argument
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using async comprehension over asyn_generator
    and return the random numbers
    """
    random_new = [new_number async for new_number in async_generator()]
    return random_new
