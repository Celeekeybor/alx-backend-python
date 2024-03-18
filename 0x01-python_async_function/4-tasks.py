#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async
mandatory
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random function n times

    Args:
        n (int): number of time wait _random should be callled.
        max_delay (int): delay period

    Returns:
        List[float]: List of all the delays in sorted order
    """
    # gather with an unpacked list of awaitables
    res = await asyncio.gather(*(task_wait_random(max_delay)
                               for _ in range(n)))

    # Sort result in ascending order
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if (res[i] > res[j]):
                res[i], res[j] = res[j], res[i]

    return res
