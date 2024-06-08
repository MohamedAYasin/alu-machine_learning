#!/usr/bin/env python3

"""
Module for representing and analyzing normal (Gaussian) distributions.

This module provides the Normal class to model normal distributions,
allowing for initialization with either raw data or specified mean and
standard deviation values. It supports basic statistical analysis on the
data, including calculating the distribution's mean and standard deviation
when given a dataset. The class is designed to handle cases where the
distribution parameters are directly provided or need to be estimated from
data, ensuring flexibility in statistical and probabilistic analysis.

Classes:
    Normal: Models a normal distribution with methods of statistical analysis.
"""


class Normal:
    """
    Represents a normal distribution.

    Attributes:
        mean (float): Mean of the distribution.
        stddev (float): Standard deviation of the distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes the Normal instance either from data or given parameters.

        Parameters:
            data (list, optional): Data to estimate the distribution params.
            mean (float, optional): Mean of the distribution. Defaults to 0.
            stddev (float, optional): Standard deviation. Defaults to 1.

        Raises:
            ValueError: For invalid standard deviation values.
            TypeError: If data is not a list.
        """
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data) / len(data))
                self.mean = mean
                summation = 0
                for x in data:
                    summation += ((x - mean) ** 2)
                stddev = (summation / len(data)) ** (1 / 2)
                self.stddev = stddev

    def z_score(self, x):
        """Calculates the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score."""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the PDF for a given x-value."""
        mean = self.mean
        stddev = self.stddev
        e = 2.7182818285
        pi = 3.1415926536
        power = -0.5 * (self.z_score(x) ** 2)
        coefficient = 1 / (stddev * ((2 * pi) ** (1 / 2)))
        pdf = coefficient * (e ** power)
        return pdf

    def cdf(self, x):
        """
        Calculates the CDF for a given x-value using a numerical approximation.
        """
        mean = self.mean
        stddev = self.stddev
        pi = 3.1415926536
        value = (x - mean) / (stddev * (2 ** (1 / 2)))
        val = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        val = val - ((value ** 7) / 42) + ((value ** 9) / 216)
        val *= (2 / (pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + val)
        return cdf
