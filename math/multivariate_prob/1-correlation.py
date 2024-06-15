#!/usr/bin/env python3
"""
This script calculates a correlation matrix
"""


# import necessary modules
import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix

    Args:
        C is a numpy.ndarray containing a correlation matrix

    Returns:
        A numpy.ndarray containing the correlation matrix

    Raise:
        TypeError: If C is not a numpy.ndarray
        ValueError: If C does not have shape(d, d)
    """
    # run checks
    if not isinstance(C, np.ndarray):
        raise TypeError('C must be a numpy.ndarray')

    if C.ndim != 2:
        raise ValueError('C must be a 2D square matrix')

    d = C.shape[0]

    if C.shape[0] != d or C.shape[1] != d:
        raise ValueError('C must be a 2D square matrix')

    # Calculate the standard deviations
    std_devs = np.sqrt(np.diag(C))

    # Calculate the correlation matrix
    correlation_matrix = C / np.outer(std_devs, std_devs)

    return correlation_matrix
