#!/usr/bin/env python3

"""
This module defines the Binomial class for representing and analyzing data
using the binomial distribution. The binomial distribution describes the
number of successes in a fixed number of independent Bernoulli trials,
each with the same probability of success.

The Binomial class can be initialized directly with the number of trials
(n) and the probability of success (p), or it can estimate these parameters
from provided data. This flexibility makes the class useful for both
theoretical studies and practical data analysis where parameters are not
known a priori.

Classes:
    Binomial: Models a binomial distribution with methods to estimate
    parameters and calculate distribution properties.
"""


class Binomial:
    """
    Represents a binomial distribution.

    This class can be initialized with specific values for the number of trials
    (n) and the probability of success (p) in each trial, or it can estimate
    these parameters from provided data.

    Attributes:
        n (int): Number of trials.
        p (float): Probability of success in each trial.
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initializes the Binomial instance.

        Parameters:
            data (list, optional): Data to estimate n and p. Defaults to None.
            n (int, optional): Number of trials. Defaults to 1.
            p (float, optional): Probability of success. Defaults to 0.5.

        Raises:
            ValueError: If n is not positive or p is not a valid probability.
            TypeError: If data is provided but is not a list.
            ValueError: If data does not contain at least two values.
        """
        if data is None:
            self._validate_parameters(n, p)
        else:
            self._estimate_parameters(data)

    def _validate_parameters(self, n, p):
        """Validates n and p parameters."""
        if n < 1:
            raise ValueError("n must be a positive value")
        if not (0 < p < 1):
            raise ValueError("p must be greater than 0 and less than 1")
        self.n = int(n)
        self.p = float(p)

    def _estimate_parameters(self, data):
        """Estimates n and p parameters from data."""
        if not isinstance(data, list):
            raise TypeError('data must be a list')
        if len(data) < 2:
            raise ValueError('data must contain multiple values')
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        self.p = 1 - variance / mean
        self.n = round(mean / self.p)
        self.p = mean / self.n

    def combination(self, n, k):
        """
        Calculates combinations of n and k.

        Parameters:
            n (int): Total number of items.
            k (int): Number of items to choose.

        Returns:
            int: Number of ways to choose k items from n items.
        """
        num = den = 1
        k = min(k, n - k)  # Take advantage of symmetry
        for i in range(1, k + 1):
            num *= n
            den *= i
            n -= 1
        return num // den

    def pmf(self, k):
        """
        Calculates the probability mass function (PMF) for k wins.

        Parameters:
            k (int): Number of successes.

        Returns:
            float: PMF value for k successes.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        binomial_coeff = self.combination(self.n, k)
        return binomial_coeff * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        Calculates the cumulative distribution function (CDF) up to k wins.

        Parameters:
            k (int): Number of successes.

        Returns:
            float: CDF value for up to k successes.
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
