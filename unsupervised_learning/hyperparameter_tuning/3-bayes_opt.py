#!/usr/bin/env python3
"""
    Hyperparameter Tuning project
"""
import numpy as np
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization():
    """ performs Bayesian optimization on a noiseless 1D Gaussian process """

    def __init__(self, f, X_init, Y_init, bounds, ac_samples,
                 l=1, sigma_f=1, xsi=0.01, minimize=True):
        """
        f is the black-box function to be optimized
        X_init ndarray (t, 1) inputs already sampled with black-box function
        Y_init ndarray (t, 1) outputs of black-box function for
            each input in X_init
        t is the number of initial samples
        bounds tuple (min, max) representing the bounds of the space
            in which to look for the optimal point
        ac_samples number of samples that should be analyzed during acquisition
        l is the length parameter for the kernel
        sigma_f is the standard deviation given to the output of
            the black-box function
        xsi is the exploration-exploitation factor for acquisition
        minimize is a bool determining whether optimization should be performed
            for minimization (True) or maximization (False)
        Sets the public instance attributes X, Y, l, and sigma_f corresponding
            to the respective constructor inputs
        Sets the public instance attribute K, representing the current
            covariance kernel matrix for the Gaussian process
        """
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        l, h = bounds
        self.X_s = np.linspace(l, h, num=ac_samples)[:, np.newaxis]
        self.xsi = xsi
        self.minimize = minimize
