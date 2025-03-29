#!/usr/bin/env python3
"""
    Policy Gradients
"""
import numpy as np
import scipy as sp
import scipy.linalg


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
    # print(probabilities[0])
    action = np.random.choice(len(probabilities[0]), p=probabilities[0])
    soft_der = softmax_grad(policy(state, weight))[action, :]
    dlog = soft_der / probabilities[0, action]
    grad = np.dot(state.T, dlog[None, :])
    return action, grad


def toeplitz_discount_rewards(rewards, gamma):
    n = len(rewards)
    c = np.zeros_like(rewards)
    c[0] = 1

    r = np.array([gamma**i for i in range(n)])
    matrix = sp.linalg.toeplitz(c, r)
    discounted_rewards = matrix @ rewards
    return discounted_rewards


def discount_rewards(episode_rewards, gamma):
    discounted_episode_rewards = np.zeros_like(episode_rewards)
    cumulative = 0.0
    for i in reversed(range(len(episode_rewards))):
        cumulative = cumulative * gamma + episode_rewards[i]
        discounted_episode_rewards[i] = cumulative
    return discounted_episode_rewards


def train(env, nb_episodes, alpha=0.000045, gamma=0.98, show_result=False):
    """ implements full training of REINFORCE
        env: initial environment
        nb_episodes: number of episodes used for training
        alpha: the learning rate
        gamma: the discount factor
        Return: all values of the score
            (sum of all rewards during one episode loop)
    """
    total_rewards = []
    states = []
    actions = []
    grads = []
    reward = 0
    weight = np.random.rand(4, 2)
    for e in range(nb_episodes):
        # print(e)
        state = env.reset()[None, :]
        rewards = []
        states = []
        actions = []
        grads = []
        reward = 0
        done = False
        while not done:
            action, grad = policy_gradient(state, weight)
            new_state, new_reward, done, info = env.step(action)
            reward += new_reward
            # weight += grad * alpha
            # print(done)
            state = new_state[None, :]
            actions.append(action)
            grads.append(grad)
            rewards.append(reward)
        total_rewards.append(reward)
        # try:
        discount = toeplitz_discount_rewards(rewards, gamma)
        # except:
        #    discount = np.array([0])
        # grad_log_p = np.array([self.grad_log_p(ob)[action]
        #   for ob,action in zip(obs,actions)])
        # discount = discount_rewards(rewards, gamma)
        # print(discount.shape, discount)
        # if len(discount) < 1:
        #    discount = 0
        # print('discount again', discount)
        # what = alpha * discount
        # print('what', what)
        # discount = toeplitz_discount_rewards(rewards, gamma)
        for i in range(len(grads)):
            weight += alpha * (np.array(grads[i]) * discount[i])
            # weight += alpha * (gamma ** i) * (rewards)
        print("Episode [{}]: Score [{}]".format(e, reward),
              end="\r", flush=False)
        if show_result and (e % 1000 == 0):
            env.render()
    return total_rewards
