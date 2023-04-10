#!/usr/bin/env python3

"""
An async routine called wait_n that takes in 2 int arguments
in order of n and max_delay.
"""

import asyncio
from typing import TYPE_CHECKING, List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes in 2 int arguments (in this order): n and max_delay,
    and will spawn wait_random n times with the specified max_delay.
    """
    task = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    result_gotten = await asyncio.gather(*task)
    return sorted(result_gotten)
