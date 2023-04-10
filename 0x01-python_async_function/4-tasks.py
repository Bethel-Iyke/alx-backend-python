#!/usr/bin/env python3
""" Alter code from the previous file to form a new function."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """takes in 2 int arguments (in this order): n and max_delay,
    and will spawn wait_random n times with the specified max_delay.
    """
    task = [await (task_wait_random(max_delay)) for i in range(n)]
    # result_gotten = await asyncio.gather(*task)
    return sorted(task)
