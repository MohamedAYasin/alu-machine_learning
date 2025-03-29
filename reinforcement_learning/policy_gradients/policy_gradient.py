#!/usr/bin/env python3
"""
    Policy Gradients
"""
import numpy as np


def softmax(z):
    # z -= np.max(z)
    sm = (np.exp(z).T / np.sum(np.exp(z).T, axis=0)).T
    return sm


def policy(matrix, weight):
    """ computes to policy with a weight matrix """
    return softmax(matrix.dot(weight))
    '''policy = []
    for i in range(len(weight)):
        policy.append(weight[i] * matrix.T[i])
        print('m', matrix.T[i])
        print('w', weight[i])
    return np.array(policy).sum(axis=0)'''


def softmax_grad(softmax):
    """ gradient of softmax """
    s = softmax.reshape(-1, 1)
    return np.diagflat(s) - np.dot(s, s.T)


def policy_gradient(state, weight):
    """ computes monte carlo policy gradient based on state and matrix
        state: matrix representing the current observation of the environment
        weight: matrix of random weight
        Return: the action and the gradient (in this order)
    """
    probabilities = policy(state, weight)
    action = np.random.choice(len(probabilities[0]), p=probabilities[0])
    soft_der = softmax_grad(policy(state, weight))[action, :]
    dlog = soft_der / probabilities[0, action]
    grad = np.dot(state.T, dlog[None, :])
    return action, grad
