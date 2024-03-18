#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random integers between 0 and max_delay

    Args:
        max_delay (int): maximum delay value

    Returns:
       awaited value
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
