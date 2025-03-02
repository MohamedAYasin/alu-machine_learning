#!/usr/bin/env python3
"""
    Clustering
"""
import sklearn.mixture


def gmm(X, k):
    """ expectation maximization
    """
    '''if type(X) is not np.ndarray or X.ndim != 2\
            or type(k) is not int or k <= 0:
        return None, None'''
    gm = sklearn.mixture.GaussianMixture(k).fit(X)

    return gm.weights_, gm.means_, gm.covariances_, gm.predict(X), gm.bic(X)
