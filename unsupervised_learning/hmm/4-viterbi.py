#!/usr/bin/env python3
"""
    Hidden Markov Models project
"""
import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
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
        Returns: path, P, or None, None on failure
            path is the a list of length T containing the most
                likely sequence of hidden states
            P is the probability of obtaining the path sequence
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
    P = .5
    F = np.ndarray((N, 1))
    return F, P
