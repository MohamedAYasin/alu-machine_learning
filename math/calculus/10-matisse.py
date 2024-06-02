#!/usr/bin/env python3
'''
Module for calculating the derivative of a polynomial.

This module provides a function poly_derivative which takes a list
of coefficients (poly) representing a polynomial. The function returns
a new list of coefficients representing the derivative of the polynomial.
'''


def poly_derivative(poly):
    '''
    Calculate the derivative of a polynomial.

    Parameters:
    poly (list): Coefficients list where index represents power of x.

    Returns:
    list: Coefficients list representing the polynomial's derivative,
          or None if input is invalid.
    '''
    # Validate input
    if not isinstance(poly, list) or not poly:
        return None
    for coefficient in poly:
        if not isinstance(coefficient, (int, float)):
            return None

    # Calculate derivative
    if len(poly) == 1:
        return [0]
    derivative = [
        coefficient * power
        for power, coefficient in enumerate(poly)
    ][1:]
    return derivative


# Example usage:
if __name__ == "__main__":
    poly = [5, 3, 0, 1]  # Represents the polynomial 5 + 3x + x^3
    print(poly_derivative(poly))  # Output: [3, 0, 3]
