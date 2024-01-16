#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Async generator that yields a random number between 0 and 10 after
    asynchronously waiting 1 second. This process is repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)