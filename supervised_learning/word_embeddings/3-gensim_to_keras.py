#!/usr/bin/env python3
"""
task 3: Function to convert gensim Word2Vec model to a keras Embedding layer
"""

from keras.layers import Embedding
import numpy as np


def gensim_to_keras(model):
    """
    Converts a trained gensim word2vec model to a keras Embedding layer.
    """
    # extracting weights from the gensim model
    weights = model.wv.vectors
    vocab_size, embedding_size = weights.shape

    # ng an additional row of zeros for handling out-of-vocabulary words
    oov_row = np.zeros((1, embedding_size))
    updated_weights = np.vstack((weights, oov_row))

    # creating a Keras Embedding layer with the extracted weights
    layer = Embedding(input_dim=vocab_size + 1, output_dim=embedding_size, 
                      trainable=True, weights=[updated_weights])

    return layer
