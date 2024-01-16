#!/usr/bin/env python3
"""
Measure Runtime

This module defines a coroutine called measure_runtime that executes
async_comprehension four times in parallel using asyncio.gather.
"""

from typing import List
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of async_comprehension
    executed four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()

    # Calculate and return the total runtime
    return end_time - start_time

# Example usage
if __name__ == "__main__":
    import asyncio

    async def main():
        return await measure_runtime()

    print(asyncio.run(main()))
