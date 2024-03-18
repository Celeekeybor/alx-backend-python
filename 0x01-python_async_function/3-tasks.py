#!/usr/bin/env python3
"""Asyncio.Task"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create task wait random

    Args:
        max_delay (int): delay period

    Returns:
        (asyncio.Task)
    """
    Task = asyncio.create_task(wait_random(max_delay))

    return Task
