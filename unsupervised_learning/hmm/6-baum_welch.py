#!/usr/bin/env python3
"""
    Hidden Markov Models project
"""
import numpy as np


def baum_welch(Observations, Transition, Emission, Initial, iterations=1000):
    """ that performs the Baum-Welch algorithm for a hidden markov model
        Observation ndarray (T,) that contains the index of the observation
            T is the number of observations
        Emission ndarray (N, M) containing the emission probability
            of a specific observation given a hidden state
            Emission[i, j] is the probability of observing
                j given the hidden state i
            N is the number of hidden states
            M is the number of all possible observations
        Transition 2D ndarray (N, N) containing the transition probabilities
        Transition[i, j] is the probability of transitioning from
            the hidden state i to j
        Initial ndarray (N, 1) containing the probability of starting in
            a particular hidden state
        Iterations is the number of times expectation-maximization
            should be performed
        Returns: the converged Transition, Emission, or None, None on failure
    """
    if type(Observations) is not np.ndarray or\
            len(Observations.shape) != 1 or\
            type(Emission) is not np.ndarray or\
            len(Emission.shape) != 2 or\
            type(Transition) is not np.ndarray or\
            len(Transition.shape) != 2 or\
            type(Initial) is not np.ndarray or\
            len(Initial.shape) != 2 or\
            type(iterations) is not int or\
            iterations < 1:
        return None, None
    N, M = Emission.shape
    T = Observations.shape[0]
    P = .5
    F = np.ndarray((N, T))
    return Transition, Emission
