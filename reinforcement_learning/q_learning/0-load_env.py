#!/usr/bin/env python3
'''
    A function def load_frozen_lake(
        desc=None, map_name=None, is_slippery=False
    ):
    that loads the pre-made FrozenLakeEnv
    evnironment from OpenAI’s gym:
'''

import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """
    loads the pre-made FrozenLakeEnv evnironment from OpenAI’s gym
    """
    return gym.make('FrozenLake-v0',
                    desc=desc,
                    map_name=map_name,
                    is_slippery=is_slippery)
