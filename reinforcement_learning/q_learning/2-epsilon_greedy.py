#!/usr/bin/env python3
'''
    A function def epsilon_greedy(Q, state, epsilon):
    that uses epsilon-greedy to determine the next action:
'''


import numpy as np 


def epsilon_greedy(Q, state, epsilon):
    p = np.random.uniform(0, 1)
    if p < epsilon:
        # exploring
        action = np.random.randint(Q.shape[1])
    else:
        # exploiting
        action = np.argmax(Q[state, :])
    return action
 