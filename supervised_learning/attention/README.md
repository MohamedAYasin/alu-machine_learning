# NLP Attention Mechanism & Transformers Project

## Resources

To understand and complete this project, you should review the following resources:

- [Attention for RNN Seq2Seq Models](#)
- [Attention Model Intuition](#)
- [Attention Model](#)
- [How Transformers work in deep learning and NLP: an intuitive introduction](#)
- [Transformers](#)
- [Bert, GPT: The Illustrated GPT-2 - Visualizing Transformer Language Models](#)
- [SQuAD](#)
- [Glue](#)
- [Self-Supervised Learning](#)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external references:

### General:
- What is the attention mechanism?
- How to apply attention to RNNs
- What is a transformer?
- How to create an encoder-decoder transformer model
- What is GPT?
- What is BERT?
- What is self-supervised learning?
- How to use BERT for specific NLP tasks
- What are SQuAD and GLUE?

## Requirements

### General:
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 16.04 LTS using Python 3 (version 3.5)
- Files will be executed with `numpy` (version 1.16) and `tensorflow` (version 1.15)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- All files must be executable
- A `README.md` file at the root of the project folder is mandatory
- Your code should follow the pycodestyle style (version 2.4)
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### TensorFlow Update:
In order to complete this project, you will need to update TensorFlow to version 1.15, which will also update numpy to version 1.16. Use the following command:

```bash
pip install --user tensorflow==1.15