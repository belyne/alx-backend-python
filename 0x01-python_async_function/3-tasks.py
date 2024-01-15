#!/usr/bin/env python3
"""
Tasks
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function syntax to create an asyncio.Task.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A Task object representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
