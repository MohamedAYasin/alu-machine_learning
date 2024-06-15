#!/usr/bin/env python3
"""
This script represents a Multivariate normal distributiion
"""


# import modules
import numpy as np


class MultiNormal():
    """
    This class reps a Multivariate Gaussian Distribution
    """

    def __init__(self, data):
        """ Init method """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError('data must be a 2D numpy.ndarray')
        d, n = data.shape

        # ensure data contains multiple data points
        if n < 2:
            raise ValueError('data must contain multiple data points')

        # set public instance variables mean and cov
        self.mean = np.mean(data, axis=1, keepdims=True)
        self.cov = np.dot((data - self.mean), (data - self.mean).T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at a data point
        """
        if not isinstance(x, np.ndarray):
            raise TypeError('x must be a numpy.ndarray')
        # d is the number of dimensions
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError('x must have the shape (' + str(d) + ', 1)')

        # get the determinant of the covariance matrix
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        pdf = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)
        mult = np.matmul(np.matmul((x - self.mean).T, inv), (x - self.mean))
        pdf *= np.exp(-0.5 * mult)
        pdf = pdf[0][0]

        return pdf
