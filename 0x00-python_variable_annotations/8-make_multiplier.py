#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a multiplier (a float) as an argument and returns a 
    function that multiplies a given float by the multiplier.
    
    Parameters:
    multiplier (float): The value by which the input float will be multiplied.
    
    Returns:
    Callable[[float], float]: A function that takes a float as input and returns 
    the result of multiplying the input by the multiplier.
    """
    
    def multiplier_func(x: float) -> float:
        """
        Multiplies the input value by the multiplier.

        Parameters:
        x (float): The value to be multiplied.
        
        Returns:
        float: The product of x and the multiplier.
        """
        return x * multiplier

    return multiplier_func
