#!/usr/bin/env python3
"""calculates the culumative n-gram BLEU score of a sentnece"""
import numpy as np
from collections import Counter


def cumulative_bleu(references, sentence, n):
    """calculates the culumative n-gram BLEU score of a sentnece"""
    def calculate_precision(candidate, references, n):
        """calcukate precision, need to add this one too"""
        c_ngrams = Counter(zip(*[sentence[i:] for i in range(n)]))
        rn = [Counter(zip(*[ref[i:] for i in range(n)])) for ref in references]

        c_counts = {}
        for ngram in c_ngrams:
            max_count = max(r_ngram[ngram] for r_ngram in rn)
            c_counts[ngram] = min(c_ngrams[ngram], max_count)

        precision = sum(c_counts.values()) / max(1, sum(c_ngrams.values()))
        return precision

    bleu_score = 1.0

    for i in range(1, n + 1):
        precision_i = calculate_precision(sentence, references, i)
        bleu_score *= precision_i

    crl = min(len(ref) for ref in references)
    b_penalty = np.exp(1 - (crl / len(sentence))) if len(sentence) < crl else 1

    bleu_score = b_penalty * bleu_score ** (1 / n)
    return bleu_score
