#!/usr/bin/env python3
"""
    Clustering
"""
import numpy as np


def pdf(X, m, S):
    """ probability density function of a Gaussian distribution
        X ndarray (n, d) dataset
            n # data points to evaluate pdf, d # dimensions
        m ndarray (d,) mean of distribution
        S ndarray (d, d) covariance of distribution
        No loops
        no n-p d-iag functions allowed
        Returns: P, or None on failure
            P ndarray (n,) containing the PDF values for each data point
            All values in P should have a minimum value of 1e-300
    """
    if type(X) is not np.ndarray or X.ndim != 2\
            or type(m) is not np.ndarray or m.ndim != 1\
            or type(S) is not np.ndarray or S.ndim != 2:
        return None
    n, d = X.shape
    if d != m.shape[0] or d != S.shape[0]\
            or S.shape[0] != S.shape[1] or d != S.shape[1]:
        return None
    det = np.linalg.det(S)
    # xm = X - m
    xm = X - m[np.newaxis, :]
    norm = 1 / (np.power(2 * np.pi, (d / 2)) * np.sqrt(det))
    inv = np.linalg.inv(S)
    res = np.exp(-0.5 * (xm @ inv @ xm.T))
    P = (norm * res)  # [0] # [0]
    P = P.reshape(len(P) ** 2)[::len(P) + 1]
    return np.where(P < 1e-300, 1e-300, P)  # np.maximum(P, 1e-300)
    '''
    # print(X.shape)
    # print(k)
    # print(det)
    # print("xm shape", xm.shape)
    # print(xm)
    # inv = np.linalg.inv(S)
    # print("inv shape", inv.shape)
    """
    norm = 1 / (2 * np.pi) ** (d / 2) * det
    res = np.exp(-.5 * (xm @ inv @ xm.T))
    # maha = np.sum(np.square(np.dot(xm, inv)), axis=-1)"""
    P = (norm * res)  # [0][0]
    P = P.reshape(len(P) ** 2)[::len(P) + 1]
    P = P.reshape(len(P) ** 2)[::len(P) + 1]
    return P
    '''
