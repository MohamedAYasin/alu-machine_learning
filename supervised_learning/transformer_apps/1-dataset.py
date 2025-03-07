#!/usr/bin/env python3
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np

class Dataset:
    """Dataset class for loading and preparing a machine translation dataset"""

    def __init__(self):
        """Initializes the Dataset instance."""
        self.data_train = tfds.load('ted_hrlr_translate/pt_to_en', split='train', as_supervised=True)
        self.data_valid = tfds.load('ted_hrlr_translate/pt_to_en', split='validation', as_supervised=True)
        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(self.data_train)

    def tokenize_dataset(self, data):
        """creates sub-word tokenizers for the dataset."""
        tokenizer_en = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            (en.numpy() for pt, en in data), target_vocab_size=2**15)
        tokenizer_pt = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
            (pt.numpy() for pt, en in data), target_vocab_size=2**15)

        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        """Encodes a translation into tokens"""
        pt_vocab_size = self.tokenizer_pt.vocab_size
        en_vocab_size = self.tokenizer_en.vocab_size

        pt_tokens = [pt_vocab_size] + self.tokenizer_pt.encode(pt.numpy()) + [pt_vocab_size + 1]
        en_tokens = [en_vocab_size] + self.tokenizer_en.encode(en.numpy()) + [en_vocab_size + 1]

        return np.array(pt_tokens), np.array(en_tokens)
