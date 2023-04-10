#!/usr/bin/env python3
"""
An asynchrnous coroutine that takes an int argument,
wait for maximum delay time and return it.
"""


import asyncio
import random
from typing import TYPE_CHECKING


async def wait_random(max_delay: int = 10) -> float:

    """
    takes in maximum delay time as int argument,
    then waits for random delay time before returning it.
    """

    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
