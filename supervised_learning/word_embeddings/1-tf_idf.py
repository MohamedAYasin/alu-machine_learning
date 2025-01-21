#!/usr/bin/env python3
"""task 1: tf_idf"""
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(sentences, vocab=None):
    """
    creating a TF-IDF embedding matrix
    """
    # init TfidfVectorizer with given vocab
    vectorizer = TfidfVectorizer(vocabulary=vocab)

    # fit and transform the sentences
    X = vectorizer.fit_transform(sentences)

    # get the feature names (vocab)
    features = vectorizer.get_feature_names()

    # converting sparse matrix to numpy array
    embeddings = X.toarray()

    return embeddings, features
