#!/usr/bin/env python3
"""
Measure time function that measures total time of excution
"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total amount of time used to execute wait_n in the previous
    file and returns the total time / n
    """
    begin_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    finish_time = time.perf_counter()
    spent_time = finish_time - begin_time
    return spent_time / n
