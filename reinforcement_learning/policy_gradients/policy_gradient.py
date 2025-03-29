#!/usr/bin/env python3
"""
A function that computes to policy
with a weight of a matrix
"""


import numpy as np


def policy(matrix, weight):
    """
    Args:
        state is a numpy.ndarray of shape (1, 4)
        weight is a numpy.ndarray of shape (4, 2)

    Returns:
        the policy for the given state and weight
    """
    # for each column of weights, sum (matrix[i] * weight[i]) using dot product
    dot_product = matrix.dot(weight)
    # find the exponent of the calculated dot product
    exp = np.exp(dot_product)
    # policy is exp / sum(exp)
    policy = exp / np.sum(exp)
    return policy


def policy_gradient(state, weight):
    """
    Args:
        state is a numpy.ndarray of shape (1, 4)
        weight is a numpy.ndarray of shape (4, 2)

    Returns:
        the gradient of the policy for the given state and weight
    """
    # first calculate policy using the policy function above
    Policy = policy(state, weight)
    # get action from policy
    action = np.random.choice(len(Policy[0]), p=Policy[0])
    # reshape single feature from policy
    s = Policy.reshape(-1, 1)
    # apply softmax function to s and access value at action
    softmax = (np.diagflat(s) - np.dot(s, s.T))[action, :]
    # calculate the dlog as softmax / policy at action
    dlog = softmax / Policy[0, action]
    # find gradient from input state matrix using dlog
    gradient = state.T.dot(dlog[None, :])
    # return action and the policy gradient
    return action, gradient
