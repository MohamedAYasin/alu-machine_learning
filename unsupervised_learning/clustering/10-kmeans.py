#!/usr/bin/env python3
"""
    Clustering
"""
import sklearn.cluster


def kmeans(X, k):
    """ expectation maximization
    """
    '''if type(X) is not np.ndarray or X.ndim != 2\
            or type(k) is not int or k <= 0:
        return None, None'''
    km = sklearn.cluster.KMeans(n_clusters=k).fit(X)
    return km.cluster_centers_, km.labels_
