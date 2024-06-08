#!/usr/bin/env python3

"""
This module provides the Exponential class for modeling and analyzing data
using the exponential distribution. It supports initializing the distribution
directly with a rate parameter (lambtha) or indirectly through data analysis.
The exponential distribution is useful in modeling the time between events
in a Poisson point process.

Classes:
    Exponential: Models an exponential distribution.
"""


class Exponential:
    """
    Represents an exponential distribution, characterized by the parameter
    lambtha, which is the expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Exponential instance with a specific lambtha value.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / float(sum(data) / len(data))

    def pdf(self, x):
        """
        Calculates the PDF value for a given time period.
        """
        if x < 0:
            return 0

        e = 2.7182818285
        return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """
        Calculates the CDF value for a given time period.

        Args:
            x (float): The time period.

        Returns:
            float: The CDF value for x, or 0 if x is out of range.
        """
        if x < 0:
            return 0

        e = 2.7182818285
        return 1 - e ** (-self.lambtha * x)
