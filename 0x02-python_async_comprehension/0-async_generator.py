#!/usr/bin/env python3
"""coroutines that takes no argument """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    loops 10times, each asynchronously wait 1 second and yeild random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
new_number = random.uniform(0, 10)
