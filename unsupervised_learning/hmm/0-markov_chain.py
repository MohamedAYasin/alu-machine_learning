#!/usr/bin/env python3
"""
    Hidden Markov Models project
"""
import numpy as np


def markov_chain(P, s, t=1):
    """ determines the probability of a markov chain being
            in a particular state after a specified number of iterations
        P square 2D ndarray (n, n) transition matrix
            P[i, j] is the probability of transitioning from state i to state j
            n is the number of states in the markov chain
        s ndarray (1, n) representing the probability of starting in each state
        t number of iterations markoc chain has been through
        Returns ndarray (1, n) representing the probability of being in a
            specific state after t iterations, or None on failure
    """
    if type(P) is not np.ndarray or P.shape[0] != P.shape[1]\
            or type(s) is not np.ndarray or s.shape != (1, P.shape[0])\
            or type(t) is not int or t < 0:
        return None
    # s = np.array([.9, .1])
    # P = np.array([[.98, .02], [.78, .22]])
    for _ in range(t):
        s = np.dot(s, P)
    # tr = P ** (t - 1)# np.power(P, t + 1)
    return s  # (P @ s.T) ** (t)
