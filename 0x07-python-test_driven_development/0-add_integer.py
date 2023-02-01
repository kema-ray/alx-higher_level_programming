#!/usr/bin/python3
"""Add Integer Module"""


def add_integer(a, b=98):
    """Add Function
    Args:
        a: first integer
        b: second integer
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: a must be an integer or b must be an integer
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    return (a + b)
