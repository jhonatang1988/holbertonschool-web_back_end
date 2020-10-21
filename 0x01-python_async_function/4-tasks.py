#!/usr/bin/env python3
"""
multiple tasks at the same time with async
"""
import asyncio
from typing import List, Tuple

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    multiple tasks at the same time with async
    :param max_delay: max delay
    :param n: times
    :return: list of random floats
    """
    randomnizers: Tuple[asyncio.Task, ...] = \
        tuple([task_wait_random(
            max_delay) for _ in range(n)])

    floats: List[float] = []

    for res in asyncio.as_completed(randomnizers):
        rnd_float = await res
        floats.append(rnd_float)

    return floats
