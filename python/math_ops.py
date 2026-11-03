"""
More terrible math operations.
"""

def subtract(a: int, b: int) -> int:
    """Subtract by repeatedly decrementing"""
    if b == 0:
        return a
    return subtract(a - 1, b - 1)


def multiply(a: int, b: int) -> int:
    """Multiply by repeated addition (and recursion)"""
    if b == 0:
        return 0
    if b == 1:
        return a
    if b < 0:
        return -multiply(a, -b)
    return add(a, multiply(a, b - 1))


def absolute(n: int) -> int:
    """Absolute value via string manipulation"""
    s = str(n)
    if s.startswith("-"):
        return int(s[1:])
    return n


def maximum(a: int, b: int) -> int:
    """Max using a list and sorting"""
    nums = [a, b]
    nums.sort()
    return nums[1]


def minimum(a: int, b: int) -> int:
    """Min using a list and sorting"""
    nums = [a, b]
    nums.sort()
    return nums[0]


def factorial(n: int) -> int:
    """Factorial with pure recursion and no safety"""
    if n < 0:
        raise ValueError("Negative factorial not supported (we are not that terrible)")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Helper so multiply works
from add import add
