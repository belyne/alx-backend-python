#!/usr/bin/env python3
"""
Measure Runtime

This module defines a coroutine called measure_runtime that executes
async_comprehension four times in parallel using asyncio.gather.
"""

from typing import List
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of async_comprehension
    executed four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for j in range(4)))

    end_time = time.time()
    return end_time - start_time
