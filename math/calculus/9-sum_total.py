jj#!/usr/bin/env python3

"""
Offers a utility to calculate the sum of squares of the first n positive
integers using a known mathematical formula, thus avoiding iterative
summation.

The `summation_i_squared` function is accurate and safe, returning None for
non-positive integer inputs. This feature renders the module useful for
mathematical and educational applications where such calculations are
common.

For examples and detailed usage, including handling of valid and invalid
inputs, see the docstring of the `summation_i_squared` function.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares of the first n positive integers using a
    specific formula to ensure efficiency and avoid iterative summation.

    Parameters:
    - n (int): Number of initial positive integers for the summation.

    Returns:
    - int or None: Sum of the squares if n is a positive integer, else None
    if n is not an integer or is non-positive.

    Example Usage:
    >>> summation_i_squared(5)
    55
    >>> summation_i_squared(-1)
    None
    """

    if not isinstance(n, int) or n <= 0:
        return None
    return n * (n + 1) * (2 * n + 1) // 6


# Example usage
# print(summation_i_squared(5))  # Should return 55
# print(summation_i_squared(-1))  # Should return None
