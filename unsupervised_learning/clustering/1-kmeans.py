#!/usr/bin/env python3
"""
    Clustering
"""
import numpy as np


def kmeans(X, k, iterations=1000):
    """ Performs k-means on dataset
        X ndarray (n, d) dataset to cluster
            n # data points, d # dimensions
        k positive int # clusters
        iterations positive int max iterations
        If no change in centroids between iterations
            function should return
        Initialized with multivariate uniform distribution
            along each dimension in d
        If a cluster contains no data points during the update
            step, reinitialize its centroid
        Min values for distribution min of X along each dim
        You should use numpy.random.uniform exactly twice
        2 loops max
        Returns: (C, clss), or (None, None) on failure
            C ndarray (k, d)  centroid means for each cluster
            clss ndarray (n,) index of the cluster in C that
                each data point belongs to
    """
    if type(X) is not np.ndarray or X.ndim != 2\
            or type(k) is not int or k <= 0\
            or type(iterations) is not int\
            or iterations <= 0:
        return None, None
    n, d = X.shape
    centroids = np.random.uniform(low=X.min(axis=0),
                                  high=X.max(axis=0),
                                  size=(k, d))

    # randint
    for i in range(iterations):
        # distances = np.array(
        # np.linalg.norm(X - c, axis=1) NOT A LOOP c theingoeshere centroids)
        # wrapped in brackets
        distances = np.linalg.norm(X - np.expand_dims(centroids, 1), axis=2)
        # print(distances.shape)
        # distances = np.sqrt(np.sum((X -
        #                     centroids[:, np.newaxis])**2, axis=2))
        # print(C)
        clss = np.argmin(distances, axis=0)
        # print('clss', clss)
        cent_current = centroids.copy()
        for c in range(k):
            '''if (X[clss == c].size == 0):
                centroids[c] = np.random.uniform(
                    low=np.min(X, axis=0),
                    high=np.max(X, axis=0),
                    size=(1, d)
                )
            else:
            '''
            if len(X[c == clss]) == 0:
                centroids[c] = np.random.uniform(low=X.min(axis=0),
                                                 high=X.max(axis=0),
                                                 size=(1, d))
            else:
                centroids[c] = np.mean(X[c == clss], axis=0)
        if np.all(cent_current == centroids):
            break
            # print(centroids[c])
    # print("n, k, d", n, k, d)
    # print('cenroids shape', centroids.shape, 'clss.shape', clss.shape)
    distances = np.linalg.norm(X - np.expand_dims(centroids, 1), axis=2)
    clss = np.argmin(distances, axis=0)
    return centroids, clss
