from typing import Tuple, List, Union

def zoom_array(lst: Tuple[Union[int, float]], factor: int = 2) -> List[Union[int, float]]:
    """
    Given a tuple `lst`, zooms each item by a given `factor`. The return value is a list with repeated elements.

    Parameters:
    lst (Tuple[Union[int, float]]): A tuple of integers or floats.
    factor (int, optional): The factor by which to repeat each element. Default is 2.

    Returns:
    List[Union[int, float]]: A list with the zoomed-in elements.
    """
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
