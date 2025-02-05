#!/usr/bin/env python3
import tensorflow as tf


def create_padding_mask(seq):
    """creates a padding mask for a sequence"""
    seq = tf.cast(tf.math.equal(seq, 0), tf.float32)
    return seq[:, tf.newaxis, tf.newaxis, :]  # (batch_size, 1, 1, seq_len)

def create_look_ahead_mask(size):
    """creates a look ahead mask to mask future tokens."""
    mask = 1 - tf.linalg.band_part(tf.ones((size, size)), -1, 0)
    return mask  # (seq_len, seq_len)

def create_masks(inputs, target):
    """creates all masks for training/validation"""
    encoder_mask = create_padding_mask(inputs)

    # used in the 1st attention block in the decoder.
    # it is used to pad and mask future tokens in the input received by the decoder.
    decoder_mask = create_padding_mask(inputs)

    # used in the 2nd attention block in the decoder.
    # it pads and masks future tokens in the target sequence.
    look_ahead_mask = create_look_ahead_mask(tf.shape(target)[1])
    dec_target_padding_mask = create_padding_mask(target)
    combined_mask = tf.maximum(dec_target_padding_mask, look_ahead_mask)

    return encoder_mask, combined_mask, decoder_mask
