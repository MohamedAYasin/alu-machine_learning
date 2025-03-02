#!/usr/bin/env python3
"""
    Clustering
"""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """ expectation maximization
    """
    '''if type(X) is not np.ndarray or X.ndim != 2\
            or type(k) is not int or k <= 0:
        return None, None'''
    linky = scipy.cluster.hierarchy.linkage(X, method='ward')
    fig = plt.figure(figsize=(15, 8))
    clusters = scipy.cluster.hierarchy.fcluster(linky, dist, criterion='distance')
    dn = scipy.cluster.hierarchy.dendrogram(linky, color_threshold=dist)
    plt.show()
    return clusters  # dn['ivl']
