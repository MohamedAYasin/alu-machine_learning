#!/usr/bin/env python3
'''
mean_cov(X) calculates the mean and variance
of a data set'''


import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.

    Args:
        X: A 2D numpy.ndarray of shape (n, d) containing the data set.

    Returns:
        A tuple containing two numpy.ndarrays:
        mean: A 1D array of shape (1, d) containing the mean of the data set.
        cov: A 2D array of shape (d, d) containing the covariance matrix.

    Raises:
        TypeError: If X is not a 2D numpy.ndarray.
        ValueError: If X contains less than 2 data points.
    """

    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    # Get the number of data points (n) and the number of dimensions (d)
    n, d = X.shape

    # Check if there are multiple data points
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Compute the mean of the data set
    mean = np.mean(X, axis=0, keepdims=True)

    # Compute the covariance matrix of the data set
    cov = np.dot((X - mean).T, X - mean) / (n - 1)

    return mean, cov
