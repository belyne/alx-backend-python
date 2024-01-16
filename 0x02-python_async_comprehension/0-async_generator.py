#!/usr/bin/env python3
"""
Async Generator

This module defines a coroutine called async_generator that loops 10 times.
Each time, it asynchronously waits for 1 second and then yields a random number
between 0 and 10 using the random module.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random numbers.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Example usage
if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
