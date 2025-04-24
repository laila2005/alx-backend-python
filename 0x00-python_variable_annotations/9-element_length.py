#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given an iterable of sequences, returns a list of tuples where each tuple contains
    the sequence and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences (like lists, strings, etc.).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
