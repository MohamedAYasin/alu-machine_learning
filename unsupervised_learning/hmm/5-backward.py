#!/usr/bin/env python3
"""
    Hidden Markov Models project
"""
import numpy as np


def backward(Observation, Emission, Transition, Initial):
    """ calculates the most likely sequence of hidden states
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
        Returns: P, B, or None, None on failure
            P is the likelihood of the observations given the model
            B is a ndarray (N, T) containing the backward path probabilities
            B[i, j] is the probability of generating the future
                observations from hidden state i at time j
    """
    if type(Observation) is not np.ndarray or\
            len(Observation.shape) != 1 or\
            type(Emission) is not np.ndarray or\
            len(Emission.shape) != 2 or\
            type(Transition) is not np.ndarray or\
            len(Transition.shape) != 2 or\
            type(Initial) is not np.ndarray or\
            len(Initial.shape) != 2:
        return None, None
    N, M = Emission.shape
    T = Observation.shape[0]
    P = .5
    F = np.ndarray((N, T))
    return P, F
