#!/usr/bin/env python3
"""
class SelfAttention that inherits from
tensorflow.keras.layers.Layer to calculate
the attention for machine translation based on this paper:
"""


import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """
    class SelfAttention that inherits from
    tensorflow.keras.layers.Layer to calculate
    the attention for machine translation
    """

    def __init__(self, units):
        """
        Class constructor
        """
        if type(units) is not int:
            raise TypeError(
                "units must be int representing the number of hidden units")
        super(SelfAttention, self).__init__()
        self.W = tf.keras.layers.Dense(units=units)
        self.U = tf.keras.layers.Dense(units=units)
        self.V = tf.keras.layers.Dense(units=1)

    def call(self, s_prev, hidden_states):
        '''
        s_prev: a tensor of shape (batch, units) containing
        the previous decoder hidden state
        hidden_states: a tensor of shape (batch, input_seq_len, units)
        containing the outputs of the decoder
        Returns: context, weights
            context: a tensor of shape (batch, units) that
            contains the attention vector for each time step
        '''
        W = self.W(tf.expand_dims(s_prev, 1))
        U = self.U(hidden_states)
        V = self.V(tf.nn.tanh(W + U))
        weights = tf.nn.softmax(V, axis=1)
        context = tf.reduce_sum(weights * hidden_states, axis=1)
        return context, weights
