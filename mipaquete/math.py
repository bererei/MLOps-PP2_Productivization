"""
This module makes simple operations with two numbers
"""

from typing import Union

numeric = Union[int, float]


def add(num1: numeric, num2: numeric) -> numeric:
    """Adds two numbers

    Args:
        num1 (numeric): First number
        num2 (numeric): Second number

    Returns:
        numeric: Addition result

    Examples:
        >>> from mipaquete.math import add
        >>> add(2.5, 2.5)
        5.0
    """
    return num1 + num2


def subtract(num1: numeric, num2: numeric) -> numeric:
    """Substracts two numbers

    Args:
        num1 (numeric): First number
        num2 (numeric): Second number

    Returns:
        numeric: Substraction result

    Examples:
        >>> from mipaquete.math import subtract
        >>> subtract(2, -3.5)
        5.5
    """
    return num1 - num2


def multiply(num1: numeric, num2: numeric) -> numeric:
    """Multiplies two numbers

    Args:
        num1 (numeric): First number
        num2 (numeric): Second number

    Returns:
        numeric: Multiplication result

    Examples:
        >>> from mipaquete.math import multiply
        >>> multiply(2.5, 1)
        2.5
    """
    return num1 * num2
