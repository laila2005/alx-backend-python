#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

# Define a TypeVar to make the function generic
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Given a dictionary, a key, and an optional default, returns the value corresponding to the key
    if it exists in the dictionary; otherwise, returns the default value.

    Parameters:
    dct (Mapping[Any, T]): A dictionary-like object with any type of keys and values of type T.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None], optional): The value to return if the key is not found. Default is None.

    Returns:
    Union[T, None]: The value corresponding to the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
