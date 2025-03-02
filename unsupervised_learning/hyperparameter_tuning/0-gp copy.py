#!/usr/bin/env python3
"""
    Hyperparameter Tuning project
"""
import numpy as np


class GaussianProcess():
    """ represents a noiseless 1D Gaussian process """

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """
        X_init ndarray (t, 1) inputs already sampled with black-box function
        Y_init ndarray (t, 1) outputs of black-box function for
            each input in X_init
        t is the number of initial samples
        l is the length parameter for the kernel
        sigma_f is the standard deviation given to the output of
            the black-box function
        Sets the public instance attributes X, Y, l, and sigma_f corresponding
            to the respective constructor inputs
        Sets the public instance attribute K, representing the current
            covariance kernel matrix for the Gaussian process
        """
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """ calculates the covariance kernel matrix between two matrices
            X1 ndarray (m, 1)
            X2 ndarray (n, 1)
            the kernel should use the Radial Basis Function (RBF)
            Returns: the covariance kernel matrix as ndarray (m, n)
        """
        sqdist = np.sum(X1 ** 2, 1).reshape(-1, 1) +\
            np.sum(X2 ** 2, 1) - 2 * np.dot(X1, X2.T)
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)

        '''
        K = np.zeros((X1.shape[0], X2.shape[0]))
        for i, x in enumerate(X1):
            for j, y in enumerate(X2):
                K[i, j] = np.exp((1 / (self.sigma_f ** 2)) *\
                     -np.linalg.norm(x - y) ** 2)
        return K'''

        print(X1.shape, X2.shape)
        sub = np.subtract(X1[:, np.newaxis], X2)
        # sub = sub[:, np.newaxis]
        print("sub.shape", sub.shape)
        distance = np.linalg.norm(X1 - X2[:, np.newaxis], axis=1) ** 2
        # distance = distance
        # distance = ((X1 - X2) @ (X1 - X2).T)
        # #np.linalg.norm((X1 - X2[:, np.newaxis]) ** 2, axis=2)
        # #((X1 - X2[:, np.newaxis]) ** 2).sum(axis=2)
        # # np.linalg.norm(X1 - X2, axis=-1)
        return np.exp(-distance / (2*self.l * self.sigma_f ** 2))
        # np.exp(- distance / (2 * (self.sigma_f ** 2)))

        inner = (-(1 / 2) * self.l ** 2) * (distance)
        return self.sigma_f ** 2 * np.exp(inner)
        # sqdist = np.sum(X1**2, 1).reshape(-1, 1) +\
        #   np.sum(X2**2, 1) - 2 * np.dot(X1, X2.T)
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)

        num = np.sqrt(np.linalg.norm(X1 - X2, axis=1))
        den = 2 * self.l ** 2
        return np.exp(-(num / den))
