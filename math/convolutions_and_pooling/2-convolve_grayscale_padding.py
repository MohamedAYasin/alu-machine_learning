#!/usr/bin/env python3
'''
    A function def convolve_grayscale_padding(images, kernel, padding):
    that performs a same convolution on grayscale images:
'''


import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
Defines a function for applying convolution with padding to grayscale images.

Parameters:
- images: numpy.ndarray (m, h, w), where 'm' is the number of images, 'h' is
  their height in pixels, and 'w' is their width in pixels.
- kernel: numpy.ndarray (kh, kw), the convolution kernel with 'kh' as its
  height and 'kw' as its width.
- padding: Tuple (ph, pw) indicating padding dimensions, with 'ph' for height
  padding and 'pw' for width padding.

Returns:
- A numpy.ndarray containing the convolved images with padding.
"""

    m = images.shape[0]
    height = images.shape[1]
    width = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    ph, pw = padding
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                    'constant', constant_values=0)
    ch = height + (2 * ph) - kh + 1
    cw = width + (2 * pw) - kw + 1
    convoluted = np.zeros((m, ch, cw))
    for h in range(ch):
        for w in range(cw):
            output = np.sum(images[:, h: h + kh, w: w + kw] * kernel,
                            axis=1).sum(axis=1)
            convoluted[:, h, w] = output
    return convoluted
