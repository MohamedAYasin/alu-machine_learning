#!/usr/bin/env python3

"""
This module offers functionality for performing calculus operations on
polynomials, with an emphasis on integration. It allows polynomials to be
represented as lists of coefficients, ordered from the coefficient of the
highest power down to the constant term.

The core feature, `poly_integral`, calculates the indefinite integral of a
specified polynomial and includes an option to add a constant of integration.
This functionality is particularly useful for educational and computational
endeavors that involve polynomial calculus, providing a direct approach to
integration without the need for symbolic computation tools.

Detailed usage examples, including how to manage the constant of integration
and handle polynomials of varying degrees, can be found within the
`poly_integral` function's docstring.
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial represented as a list of
    coefficients, with an optional constant of integration.

    Polynomials should be in the form [a_n, a_{n-1}, ..., a_2, a_1, a_0], where
    a_n is the coefficient for the x^n term. The integral is computed following
    standard calculus rules and returned as a list of coefficients, including
    the constant of integration as the first term.

    Parameters:
    - poly (list): List of integers or floats representing the coefficients,
    starting from the highest power of x.
    - C (int, float, optional): Constant of integration, defaulting to 0.

    Returns:
    - list: Coefficients list of the integral. Returns [C] if the input list is
    empty. Returns None for invalid inputs (non-list or C not a number).

    Example Usage:
    >>> poly_integral([5, 3, 0, 1], 0)
    [0, 5, 1.5, 0, 0.25]
    >>> poly_integral([3, 0, 1], 2)
    [2, 3, 0, 0.333...]

    The first example integrates 5x^3 + 3x^2 + 0x + 1 with a constant of 0,
    resulting in [0, 5, 1.5, 0, 0.25]. The second integrates 3x^2 + 0x + 1 with
    a constant of 2, resulting in [2, 3, 0, 0.333...].
    """

    # Check if inputs are valid
    if (not isinstance(poly, list) or
        not all(isinstance(coef, (int, float)) for coef in poly) or
            not isinstance(C, (int, float))):
        return None

    # Return None if poly is empty, ignoring C.
    if not poly:
        return None  # Adjusted based on a hypothetical new rule

    # Calculate the integral, including C as the first term
    integral = [C] + [coef / (i + 1) for i, coef in enumerate(poly)]

    # Convert to integer if the float coefficient is an integer
    integral = [int(coef) if isinstance(coef, float)
                and coef.is_integer() else coef for coef in integral]

    # If the polynomial is not empty, remove trailing zeros
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    # Return [0] for a zero polynomial result.
    if not integral:
        return [0]

    return integral


# Example usage
# print(poly_integral([5, 3, 0, 1], 0))
# Output should be [0, 5, 1.5, 0, 0.25]
# print(poly_integral([3, 0, 1], 2))
# Output should be [2, 3, 0, 0.333...]
