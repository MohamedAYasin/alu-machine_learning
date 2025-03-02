#!/usr/bin/env python3
"""PCA on a dataset"""
import numpy as np


def pca(X, var=0.95):
    """PCA on a dataset"""
    # calculatign the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # performign eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # sorting the  eigenvalues and the corresponding eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # clalculating the cumulative sum of eigenvalues...
    # ...to maintain the given variance
    cumul_eigenvalues = np.cumsum(sorted_eigenvalues)
    total_eigenvalues = np.sum(sorted_eigenvalues)
    threshold_value = total_eigenvalues * var

    # finding the number of principal components needed
    num_components = np.argmax(cumul_eigenvalues >= threshold_value) + 1

    # constructed the weights matrix "W"
    W = sorted_eigenvectors[:, :num_components]

    # adjusting the sign of eigenvectosr
    max_abs_cols = np.argmax(np.abs(W), axis=0)
    signs = np.sign(W[max_abs_cols, range(W.shape[1])])
    W *= signs

    return W
