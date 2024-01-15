#!/usr/bin/env python3
"""
Measure the runtime
"""

import time
from typing import List
from asyncio import run
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: Total execution time / n.
    """
    start_time = time.time()

    # Run the asynchronous coroutine using asyncio.run
    run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
