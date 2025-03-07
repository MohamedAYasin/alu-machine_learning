#!/usr/bin/env python3
"""
    Autoencoders
"""
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """ creates an autoencoder
        input_dims is an integer containing the dimensions of the model input
        hidden_layers is a list containing the number of nodes for each
            hidden layer in the encoder, respectively
        the hidden layers should be reversed for the decoder
        latent_dims is an integer containing the dimensions of the latent
            space representation
        Returns: encoder, decoder, auto
            encoder is the encoder model
            decoder is the decoder model
            auto is the full autoencoder model
    """
    inputs = keras.Input(shape=(input_dims,))
    layer_enc = keras.layers.Dense(hidden_layers[0], activation='relu')(inputs)
    for hl in range(1, len(hidden_layers)):
        layer_enc = keras.layers.Dense(hidden_layers[hl],
                                       activation='relu')(layer_enc)
    latent_enc = keras.layers.Dense(latent_dims, activation='relu')(layer_enc)

    encoded_input = keras.Input(shape=(latent_dims,))
    # print('hl first', hl)
    latent = keras.layers.Dense(hidden_layers[hl],
                                activation='relu')(encoded_input)
    c = 1
    for hl in range(len(hidden_layers) - 2, -1, -1):
        # print('hl', hl)
        decod = keras.layers.Dense(hidden_layers[hl],
                                   activation='relu')(latent if c else decod)
        c = 0
    decoded = keras.layers.Dense(input_dims, activation='sigmoid')(decod)

    encoder = keras.Model(inputs, latent_enc)
    # decoder_layer = auto.layers[-1]
    # keras.layers.Dense(latent_dims, activation='sigmoid')  # auto.layers[-1]
    decoder = keras.Model(encoded_input, decoded)

    outputs = decoder(encoder(inputs))
    auto = keras.Model(inputs, outputs)
    auto.compile(optimizer='adam', loss='binary_crossentropy')
    return encoder, decoder, auto
