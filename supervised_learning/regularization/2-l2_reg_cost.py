#!/usr/bin/env python3
'''
Regularize
'''


import tensorflow as tfn


def l2_reg_cost(cost):
    """
    Calculates the cost of a neural network with L2 regularization
    """

    l2_cost = cost + tf.losses.get_regularization_losses()

    return l2_cost
