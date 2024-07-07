# The Convolutional Neural Networks (CNN) Project

## Resources

### Read or Watch:

- [Image Kernels](https://intranet.aluswe.com/rltoken/w4x7g1I2JC1GMWYlwWVGEg)
- [Understanding Convolutional Layers](https://intranet.aluswe.com/rltoken/9_9Qc0tHPYSvtBxTXr84xw)
- [A Comprehensive Guide to Convolutional Neural Networks - the ELI5 way](https://intranet.aluswe.com/rltoken/2TcwTfZpldecl5rWfA42Og)
- [What is max pooling in convolutional neural networks?](https://intranet.aluswe.com/rltoken/TUCIaENFK4m83ev3ImE69Q)
- [Edge Detection Examples](https://intranet.aluswe.com/rltoken/G_ST0DHZEmodIEs2racyTw)
- [Padding](https://intranet.aluswe.com/rltoken/H4PDn4iS6u4g9lIJ883MgA)
- [Strided Convolutions](https://intranet.aluswe.com/rltoken/0uejU-wovXn_sZy2tSTGhQ)
- [Convolutions over Volumes](https://intranet.aluswe.com/rltoken/Q-kqVj9FpqA2ODXTEqF5nQ)
- [Pooling Layers](https://intranet.aluswe.com/rltoken/ob1Xz9w3KqDbCIHtdIlH-g)
- [Implementing ‘SAME’ and ‘VALID’ padding of Tensorflow in Python](https://intranet.aluswe.com/rltoken/L2rzLJ4MeYZb0MKLb4vGBQ) (Note: There is a mistake regarding valid padding in this document. Floor rounding should be used for valid padding instead of ceiling.)

### Definitions to Skim:

- Convolution
- Kernel (image processing)

### References:

- [numpy.pad](https://intranet.aluswe.com/rltoken/5WoDWoJrbPpWnynQ8sy0lQ)
- [A guide to convolution arithmetic for deep learning](https://intranet.aluswe.com/rltoken/1GQlFOut1Xpy3_MAxfNSew)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What is a convolution?
- What is max pooling? average pooling?
- What is a kernel/filter?
- What is padding?
- What is “same” padding? “valid” padding?
- What is a stride?
- What are channels?
- How to perform a convolution over an image
- How to perform max/average pooling over an image

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
- Your files will be executed with numpy (version 1.15)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Unless otherwise noted, you are not allowed to import any module except `import numpy as np` and `from math import ceil, floor`
- You are not allowed to use `np.convolve`
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info

### Testing

Please download this [dataset](#) for use in some of the following main files.
