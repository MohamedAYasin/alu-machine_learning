#!/usr/bin/env python3
"""
1-ngram_bleu.py - module that calculates the n-gram BLEU score for a sentence
"""

import numpy as np
from collections import Counter


def ngram_bleu(references, sentence, n):
    """
    This emthod calculates the n-gram BLEU score for a sentence.
    """
    c_ngrams = Counter(zip(*[sentence[i:] for i in range(n)]))
    r_n = [Counter(zip(*[ref[i:] for i in range(n)])) for ref in references]

    clipped_counts = {}
    for ngram in c_ngrams:
        max_count = max(r_ngram[ngram] for r_ngram in r_n)
        clipped_counts[ngram] = min(c_ngrams[ngram], max_count)

    precision = sum(clipped_counts.values()) / max(1, sum(c_ngrams.values()))

    crlen = min(len(ref) for ref in references)

    b_pen = np.exp(1 - (crlen / len(sentence))) if len(sentence) < crlen else 1

    bleu_score = b_pen * precision

    return bleu_score
