#!/usr/bin/env python3
"""
The Module provides an asynchronous generator function that yields a
random float between 0 and 10 after a one second delay for a total of
10 iterations.
"""
import asyncio
import random
from typing import AsyncGenerator  # Import AsyncGenerator instead of Generator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator function that yields a random float between 0 and 10
    after a one second delay for a total of 10 iterations.

    Returns:
        AsyncGenerator: Asynchronous generator object that can be used in an
        awaitable context.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

