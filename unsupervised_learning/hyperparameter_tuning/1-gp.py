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

    def predict(self, X_s):
        """ predicts the mean and standard deviation of
                points in a Gaussian process
            X_s ndarray (s, 1) containing all of the points whose mean and
                standard deviation should be calculated
            s is the number of sample points
            Returns: mu, sigma
            mu ndarray (s,) containing the mean for each point
                in X_s, respectively
            sigma ndarray (s,) containing the variance for each point
                in X_s, respectively
        """
        # print(X_s.shape)
        # print(X_s)
        K = self.K
        K_s = self.kernel(self.X, X_s)
        K_ss = self.kernel(X_s, X_s)
        K_inv = np.linalg.inv(K)
        # mu = np.mean(X_s, axis=1)
        sigma = np.var(X_s)
        # x_inv = np.linalg.inv(X_s)
        mu = K_s.T.dot(K_inv).dot(self.Y)
        sigma = K_ss - K_s.T.dot(K_inv).dot(K_s)
        return mu.flatten(), np.diag(sigma)
