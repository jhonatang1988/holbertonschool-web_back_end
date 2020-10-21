#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
import time
from typing import Generator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def loops(n: int) -> Generator[int, None, None]:
    """
    generator to create async comprenhesion
    :param n: times
    :return: generator, yields int
    """
    for i in range(n):
        yield i


async def measure_runtime() -> float:
    """
    Run time for four parallel comprehensions
    :return: total runtime
    """
    start: float = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed: float = time.time() - start
    return elapsed
