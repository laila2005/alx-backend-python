#!/usr/bin/env python3
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Given a sequence (e.g., list or tuple), returns the first element if the sequence is not empty, 
    otherwise returns None.
    
    Parameters:
    lst (Sequence[Any]): A sequence (like list, tuple, etc.) with unknown element types.
    
    Returns:
    Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
