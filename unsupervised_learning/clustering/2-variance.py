#!/usr/bin/env python3
"""
    Clustering
"""
import numpy as np


def variance(X, C):
    """ Calculates the total intra-cluster variance
        X ndarray (n, d) dataset to cluster
            n # data points, d # dimensions
        C ndarray (k, d) centroid means for each cluster
            k # data points, d # dimensions
        Returns: var, or None on failure
            var is the total variance
    """
    if type(X) is not np.ndarray or X.ndim != 2\
            or type(C) is not np.ndarray or C.ndim != 2:
        return None
    try:
        k, d = C.shape
        # print("cshape", C.shape)
        '''n, _ = X.shape
        k, d = C.shape'''
        distances = np.linalg.norm(X - np.expand_dims(C, 1), axis=-1)
        # print(distances.shape)
        min = np.min(distances, axis=0)
        # print(min)
        return np.sum(np.square(min))
    except Exception:
        return None
