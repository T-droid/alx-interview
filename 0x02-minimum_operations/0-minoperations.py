#!/usr/bin/env python3
"""definition of mini_operation"""


def minOperation(n: float) -> int:
    """finds the minum operations to be perfomed on a file"""
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1
    if len(factors) == 1:
        return 0
    return (sum(factors))


print(minOperation(12))
