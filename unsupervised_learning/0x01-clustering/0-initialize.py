#!/usr/bin/env python3
"""
    Clustering
"""
import numpy as np


def initialize(X, k):
    """ Initialized cluster centroids for K-means
        X ndarray (n, d) dataset to cluster
        n # data points, d # dimensions
        k positive int # clusters
        Initialized with multivariate uniform distribution
            along each dimension in d
        Min values for distribution min of X along each dim
        Same for max
        No loops allowed
        Returns: ndarray (k, d) initialized centroids for each cluster
            or None on failure
    """
    if type(X) is not np.ndarray or X.ndim != 2\
            or type(k) is not int or k <= 0:
        return None
    n, d = X.shape
    init = np.random.uniform(low=X.min(axis=0),
                             high=X.max(axis=0),
                             size=(k, d))
    return init
