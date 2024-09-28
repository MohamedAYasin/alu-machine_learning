# Resources

## Read or Watch:

- [Hyperparameter (machine learning)](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning))
- [Feature scaling](https://en.wikipedia.org/wiki/Feature_scaling)
- [Why, How and When to Scale your Features](https://medium.com/greyatom/why-how-and-when-to-scale-your-features-4b30ab09db5e)
- [Normalizing your data](https://www.jeremyjordan.me/batch-normalization/)
- [Moving average](https://en.wikipedia.org/wiki/Moving_average)
- [An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/)
- [A Gentle Introduction to Mini-Batch Gradient Descent and How to Configure Batch Size](https://machinelearningmastery.com/gentle-introduction-mini-batch-gradient-descent-configure-batch-size/)
- [Stochastic Gradient Descent with momentum](https://towardsdatascience.com/stochastic-gradient-descent-with-momentum-a84097641a5d)
- [Understanding RMSprop](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)
- [Adam](https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c)
- [Learning Rate Schedules](https://towardsdatascience.com/learning-rate-schedules-and-adaptive-learning-rate-methods-for-deep-learning-2c8f433990d1)

### deeplearning.ai videos (Note: I suggest watching these videos at 1.5x - 2x speed):

- [Normalizing Inputs](https://www.youtube.com/watch?v=FDCfw-YqWTE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=10)
- [Mini Batch Gradient Descent](https://www.youtube.com/watch?v=4qJaSmvhxi8&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=16)
- [Understanding Mini-Batch Gradient Descent](https://www.youtube.com/watch?v=-_4Zi8fCZO4&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=17)
- [Exponentially Weighted Averages](https://www.youtube.com/watch?v=lAq96T8FkTw&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=18)
- [Understanding Exponentially Weighted Averages](https://www.youtube.com/watch?v=NxTFlzBjS-4&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=19)
- [Bias Correction of Exponentially Weighted Averages](https://www.youtube.com/watch?v=lWzo8CajF5s&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=20)
- [Gradient Descent With Momentum](https://www.youtube.com/watch?v=k8fTYJPd3_I&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=21)
- [RMSProp](https://www.youtube.com/watch?v=_e-LFe_igno&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=22)
- [Adam Optimization Algorithm](https://www.coursera.org/lecture/deep-neural-network/adam-optimization-algorithm-YKdHf)
- [Learning Rate Decay](https://www.youtube.com/watch?v=QzulmoOg2JE&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=24)
- [Normalizing Activations in a Network](https://www.youtube.com/watch?v=tNIpEZLv_eg&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=28)
- [Fitting Batch Norm Into Neural Networks](https://www.youtube.com/watch?v=em6dfRxYkYU&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=29)
- [Why Does Batch Norm Work?](https://www.youtube.com/watch?v=nUUqwaxLnWs&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=30)
- [Batch Norm At Test Time](https://www.youtube.com/watch?v=5qefnAek8OA&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=31)
- [The Problem of Local Optima](https://www.youtube.com/watch?v=fODpu1-lNTw&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc&index=34)

## References:

- [numpy.random.permutation](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.permutation.html)
- [tf.nn.moments](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/nn/moments.md)
- [tf.train.MomentumOptimizer](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/train/MomentumOptimizer.md)
- [tf.train.RMSPropOptimizer](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/train/RMSPropOptimizer.md)
- [tf.train.AdamOptimizer](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/train/AdamOptimizer.md)
- [tf.nn.batch_normalization](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/nn/batch_normalization.md)
- [tf.train.inverse_time_decay](https://github.com/tensorflow/docs/blob/r1.12/site/en/api_docs/python/tf/train/inverse_time_decay.md)

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What is a hyperparameter?
- How and why do you normalize your input data?
- What is a saddle point?
- What is stochastic gradient descent?
- What is mini-batch gradient descent?
- What is a moving average? How do you implement it?
- What is gradient descent with momentum? How do you implement it?
- What is RMSProp? How do you implement it?
- What is Adam optimization? How do you implement it?
- What is learning rate decay? How do you implement it?
- What is batch normalization? How do you implement it?

# Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
- Your files will be executed with numpy (version 1.15) and tensorflow (version 1.12)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.4)
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Unless otherwise noted, you are not allowed to import any module except `import numpy as np` and/or `import tensorflow as tf`
- You should not import any module unless it is being used
- You are not allowed to use the keras module in tensorflow
- All your files must be executable
- The length of your files will be tested using `wc`

# More Info

[The Link of the Medium Post I wrote about this project:](https://medium.com/@m.yasin/the-principal-goal-of-machine-learning-is-to-create-a-model-that-performs-well-and-gives-accurate-d266e5aef33a)

### Testing

Please use the following checkpoints to accompany the following tensorflow main files. You do not need to push these files to GitHub. Your code will not be tested with these files.

- `graph.ckpt.data-00000-of-00001`
- `graph.ckpt.index`
- `graph.ckpt.meta`
