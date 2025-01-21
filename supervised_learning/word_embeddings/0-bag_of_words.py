#!/usr/bin/env python3
"""task 0: bag_of_words"""
import numpy as np
import re


def bag_of_words(sentences, vocab=None):
    """
    Creates a bag of words embedding matrix.
    """
    # preprocess sentences: lowercase and remove punctuation
    if vocab is None:
        words_set = set()
        for sentence in sentences:
            words_set.update(re.findall(r"\b\w+(?<!'s)\b", sentence.lower()))
        vocab = sorted(words_set)

    vocab_dict = {word: i for i, word in enumerate(vocab)}
    embeddings = np.zeros((len(sentences), len(vocab)), dtype=int)

    for i, sentence in enumerate(sentences):
        for word in re.findall(r"\b\w+(?<!'s)\b", sentence.lower()):
            if word in vocab_dict:
                embeddings[i, vocab_dict[word]] += 1

    return embeddings, vocab
