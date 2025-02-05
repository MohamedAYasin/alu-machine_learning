#!/usr/bin/env python3
"""
Defines a function that calculates the positional encoding for a transformer
"""


import numpy as np


def get_angle(pos, i, dm):
    """
    Calculates the angle for the positional encoding
    """
    angle_rates = 1 / (10000 ** (i / dm))
    return pos * angle_rates


def positional_encoding(max_seq_len, dm):
    """
    Calculates the positional encoding
    """
    positional_encoding = np.zeros([max_seq_len, dm])

    for pos in range(max_seq_len):
        for i in range(0, dm, 2):
            # sin for even indices of positional_encoding
            positional_encoding[pos, i] = np.sin(get_angle(pos, i, dm))
            # cos for odd indices of positional_encoding
            positional_encoding[pos, i + 1] = np.cos(get_angle(pos, i, dm))
    return positional_encoding
