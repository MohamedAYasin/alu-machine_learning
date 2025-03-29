#!/usr/bin/env python3
"""
Defines function that initializes the Q-table with environment instance
"""


import numpy as np
import gym


def q_init(env):
    """
    function def q_init(env):
    that initializes the Q-table:
    """
    return np.zeros((env.observation_space.n, env.action_space.n))
