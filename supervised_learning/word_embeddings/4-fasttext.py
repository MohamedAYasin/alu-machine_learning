#!/usr/bin/env python3
"""
task 4: a function to create and train a gensim FastText model
"""

from gensim.models import FastText


def fasttext_model(sentences, size=100, min_count=5, negative=5, window=5, cbow=True, iterations=5, seed=0, workers=1):
    """
    creates and trains a gensim FastText model.
    """
    sg = 0 if cbow else 1
    model = FastText(size=size, window=window, min_count=min_count, workers=workers, sg=not cbow, seed=seed,
                     iter=iterations, negative=negative)
    model.build_vocab(sentences)
    model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)

    return model
