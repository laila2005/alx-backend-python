#!/usr/bin/env python3
"""Async comprehension module."""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [i async for i in async_generator()]
