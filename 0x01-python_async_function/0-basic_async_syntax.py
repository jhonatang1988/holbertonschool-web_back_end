#!/usr/bin/env python3
"""
basic async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """
    basic async
    :param max_delay: max delay
    :return: random float
    """
    rnd: float = random.uniform(0, max_delay)

    await asyncio.sleep(rnd)

    return rnd
