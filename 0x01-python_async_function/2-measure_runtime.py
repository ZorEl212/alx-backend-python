#!/usr/bin/env python3
"""Measure runtime example"""
import asyncio
import time
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """Measures the runtime of wait_n"""
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    return end - start
