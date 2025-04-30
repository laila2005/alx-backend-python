#!/usr/bin/env python3
"""Async generator module."""

import asyncio
import random


async def async_generator():
    """
    Yield 10 random numbers between 0 and 10.

    Each number is yielded after a 1-second asynchronous delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
