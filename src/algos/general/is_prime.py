"""_summary_
"""
from math import sqrt


def is_prime(num: int) -> bool:
    """_summary_

    Args:
        num (int): _description_

    Returns:
        bool: _description_
    """
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True
