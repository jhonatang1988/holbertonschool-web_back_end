#!/usr/bin/env python3
"""
multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    the main
    :param max_delay: max delay
    :param n: times
    :return: list of random floats
    """
    randomnizers = tuple([asyncio.create_task(wait_random(max_delay)) for _ in
                          range(n)])

    floats: List[float] = []

    for res in asyncio.as_completed(randomnizers):
        rnd_float = await res
        floats.append(rnd_float)

    return floats
