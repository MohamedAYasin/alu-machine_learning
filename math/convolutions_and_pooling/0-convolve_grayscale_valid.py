#!/usr/bin/env python3
"""
    Function def convolve_grayscale_valid
    convolve_grayscale_valid(images, kernel)
"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
Parameters:
- images: numpy.ndarray of shape (i, y, x), where it contains multiple grayscl
  images. Here, 'm' denotes the number of images, 'y' is the height in pixels,
  and 'x' is the width in pixels of the images.
- kernel: numpy.ndarray with shape (m, n), containing the convolution kernel.
  'kh' represents the kernel's height, and 'kw' is the kernel's width.

Returns:
- A numpy.ndarray containing the convolved images.
"""

    m, n = kernel.shape
    if m == n:
        i, y, x = images.shape
        y = y - m + 1
        x = x - m + 1
        convolved_image = np.zeros((i, y, x))
        for i in range(y):
            for j in range(x):
                shadow_area = images[:, i:i + m, j:j + n]
                convolved_image[:, i, j] = \
                    np.sum(shadow_area * kernel, axis=(1, 2))
    return convolved_image
