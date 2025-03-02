#!/usr/bin/env python3
"""
    Autoencoders
"""
import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """ creates a convolutional autoencoder
        input_dims is an integer containing the dimensions of the model input
        filters is a list containing the number of filters for each
            convolutional layer in the encoder, respectively
        the filters should be reversed for the decoder
        latent_dims is a tuple of integers containing the dimensions
            of the latent space representation
        Each convolution in the encoder should use a kernel size of (3, 3)
            with same padding and relu activation, followed by max pooling
            of size (2, 2)
        Each convolution in the decoder, except for the last two, should use a
            filter size of (3, 3) with same padding and relu activation,
            followed by upsampling of size (2, 2)
        The second to last convolution should instead use valid padding
        The last convolution should have the same number of filters as number
            of channels in input_dims with sigmoid activation and no upsampling
        Returns: encoder, decoder, auto
            encoder is the encoder model
            decoder is the decoder model
            auto is the full autoencoder model
    """
    inputs = keras.Input(shape=(input_dims))
    layer_enc = keras.layers.Conv2D(filters[0], (3, 3), activation='relu',
                                    padding='same')(inputs)
    layer_enc = keras.layers.MaxPooling2D((2, 2), padding='same')(layer_enc)
    for hl in range(1, len(filters)):
        layer_enc = keras.layers.Conv2D(filters[hl], (3, 3),
                                        activation='relu',
                                        padding='same')(layer_enc)
        # if hl != len(filters) - 1:
        layer_enc = keras.layers.MaxPooling2D((2, 2),
                                              padding='same')(layer_enc)
    # reg = keras.regularizers.l1(lambtha)
    # layer_enc = keras.layers.Flatten()(layer_enc)
    # latent_enc = keras.layers.Dense(latent_dims[2], activation='relu',
    #                                 )(layer_enc)
    # latent_enc = keras.layers.MaxPooling2D((2, 2),
    #                                        padding='same')(latent_enc)

    encoded_input = keras.Input(shape=(latent_dims))
    latent = keras.layers.Conv2D(filters[hl], (3, 3),
                                 activation='relu',
                                 padding='same')(encoded_input)
    latent = keras.layers.UpSampling2D((2, 2))(latent)
    c = 1
    for hl in range(len(filters) - 2, -1, -1):
        # reg = keras.regularizers.l1(lambtha)
        p = 'same' if hl is not 0 else 'valid'
        # print(p, hl)
        decod = keras.layers.Conv2D(filters[hl], (3, 3),
                                    activation='relu',
                                    padding=p
                                    )(latent if c else decod)
        decod = keras.layers.UpSampling2D((2, 2))(decod)
        c = 0
    decoded = keras.layers.Conv2D(input_dims[2], (3, 3), activation='sigmoid',
                                  padding='same')(decod)

    encoder = keras.Model(inputs, layer_enc)
    decoder = keras.Model(encoded_input, decoded)

    outputs = decoder(encoder(inputs))
    auto = keras.Model(inputs, outputs)
    auto.compile(optimizer='adam', loss='binary_crossentropy')
    return encoder, decoder, auto
