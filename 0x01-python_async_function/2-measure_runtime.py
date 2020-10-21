#!/usr/bin/env python3
"""
measure de runtime
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure de runtime
    :param n: times
    :param max_delay: max delay
    :return: average runtime
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.time() - start

    return total_time / n
