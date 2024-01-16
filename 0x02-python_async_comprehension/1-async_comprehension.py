#!/usr/bin/env python3
"""
Async Comprehension

This module defines a coroutine called async_comprehension that collects
10 random numbers using an async comprehension over async_generator.
"""

from typing import List
from itertools import islice

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list containing 10 random floats between 0 and 10.
    """
    return [i async for i in islice(async_generator(), 10)]

# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():
        print(await async_comprehension())

    asyncio.run(main())
