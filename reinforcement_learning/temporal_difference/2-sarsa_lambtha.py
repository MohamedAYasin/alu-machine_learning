#!/usr/bin/env python3
"""
    Temporal Difference
"""
import numpy as np


def epsilon_greedy(env, Q, state, epsilon):
    ''' performs epsilon greedy policy '''
    action = 0
    if np.random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])
    return action


def sarsa_lambtha(env, Q, lambtha, episodes=5000,
                  max_steps=100, alpha=0.1, gamma=0.99,
                  epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """
        performs the TD(λ) algorithm

        env is the openAI environment instance
        Q is a numpy.ndarray of shape (s,) containing the Q table
        lambtha is the elgibility trace factor
        episodes is the total number of episodes to train over
        max_steps is the maximum number of steps per episode
        alpha is the learning rate
        gamma is the discount rate
        epsilon is the initial threshold for epsilon greedy
        min_epsilon is the min value epsilon should decay to
        epsilon_decay is decay rate for updating epsilon between episodes
        Returns: Q, the updated value estimate
    """
    # print(V)
    initial_epsilon = epsilon
    states = Q.shape[0]
    elig = np.zeros(Q.shape)
    # se = set()
    for i in range(episodes):
        s = env.reset()
        action = epsilon_greedy(env, Q, s, epsilon)
        # break
        # episode = []
        # elig = np.zeros(states)
        for j in range(max_steps):
            # action = policy(s)
            s_new, reward, done, info = env.step(action)

            action_new = epsilon_greedy(env, Q, s, epsilon)
            # episode.append([s, action, reward, s_new])
            # elig[s] *= lambtha * gamma
            # elig += 1.0
            # elig[s, :] *= 0
            elig *= gamma * epsilon
            elig[s, action] += (1.0)  # - epsilon)

            # se.add(s)
            delta = reward + gamma * Q[s_new, action_new] - Q[s, action]
            Q += alpha * delta * elig  # * epsilon
            # for si in range(len(V)):
            # print(V.shape, elig.shape)
            if done:
                break  # s = env.reset()
            else:
                s = s_new
                action = action_new
        if epsilon < min_epsilon:
            epsilon = min_epsilon
        else:
            epsilon *= initial_epsilon * np.exp(-epsilon_decay * i)
        # print(se)
    return Q
