#!/usr/bin/env python3
"""
    Hyperparameter Tuning project
"""
import numpy as np
from scipy.stats import norm
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

    def acquisition(self):
        """ calculates the next best sample location using the
                Expected Improvement acquisition function
            Returns: X_next, EI
                X_next ndarray (1,) representing the next best sample point
                EI ndarray (ac_samples,) containing the expected improvement
                    of each potential sample
        """
        mu, sigma = self.gp.predict(self.X_s)
        mu = mu.flatten()
        # mu_sample, _ = self.gp.predict(self.(self.X_s))
        mu_sample, _ = self.gp.predict(self.gp.X)
        sigma = np.maximum(1e-15, sigma.flatten())
        if self.minimize is True:
            mu_sample_opt = np.min(self.gp.Y)
            sign = -1
        else:
            mu_sample_opt = np.max(mu)
            sign = 1
        with np.errstate(divide='warn'):
            imp = sign * (mu - mu_sample_opt + self.xsi)
            Z = imp / sigma
            ei = imp * norm.cdf(Z) + sigma * norm.pdf(Z)
        return np.array(self.X_s[np.argmax(ei)]), ei

    def optimize(self, iterations=100):
        """ optimizes the black-box function
        iterations is the maximum number of iterations to perform
        optimization should be stopped early if next
            proposed point already sampled
        Returns: X_opt, Y_opt
            X_opt ndarray (1,) representing the optimal point
            Y_opt ndarray (1,) representing the optimal function value
        """
        if type(iterations) is not int or iterations < 1:
            return None, None
        # return None, None
        bests = []
        x = []
        for i in range(iterations):
            X_next, ei = self.acquisition()
            x.append(X_next)
            bests.append(self.f(X_next))
            if X_next in self.gp.X:
                break
            self.gp.update(X_next, self.f(X_next))
        if self.minimize:
            X_next = x[np.argmin(bests)]
        else:
            X_next = x[np.argmax(bests)]
        return X_next, self.f(X_next)
