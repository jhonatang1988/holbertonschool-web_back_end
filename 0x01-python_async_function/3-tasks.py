#!/usr/bin/env python3
"""
tasks
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    tasks
    :param max_delay: max delay
    :return: an asyncio task
    """
    return asyncio.Task(wait_random(max_delay))
