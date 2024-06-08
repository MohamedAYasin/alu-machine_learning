#!/usr/bin/env python3

"""
Module for Poisson distribution properties via the Poisson class.

This module enables analyzing the Poisson distribution, which represents
the likelihood of a number of events occurring within a fixed time frame,
assuming a constant rate of occurrence (lambda) and independence of events.
It allows initializing the distribution based on data or a specific lambda
value and offers methods to compute the probability mass function (PMF) and
cumulative distribution function (CDF) for specified occurrence counts.

The PMF method calculates the probability of observing an exact number of
successes, while the CDF method provides the probability of observing up to
a certain number of successes, enriching the distribution's analytical scope.

Classes:
    Poisson: Facilitates PMF and CDF calculations for Poisson distributions.
"""


class Poisson:
    """
    Represents a Poisson distribution, characterized by lambtha, the expected
    number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson instance with data or a specific lambtha value.
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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the PMF value for a given number of successes.
        """
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        pmf_value = (self.lambtha ** k) * (e ** (-self.lambtha)) / factorial
        return pmf_value

    def cdf(self, k):
        """
        Calculates the CDF value for a given number of successes.

        Args:
            k (int): The number of successes.

        Returns:
            float: The CDF value for k.
        """
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)

        return cdf_value
