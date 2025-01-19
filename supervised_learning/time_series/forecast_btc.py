#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.layers import Masking
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load preprocessed data
bitstamp_data = np.load('/content/bitstamp_preprocessed_data_v2.npy')
coinbase_data = np.load('/content/coinbase_preprocessed_data_v2.npy')

# calculating the number of features
n = bitstamp_data.shape[1]
print(f"Number of features: {n}")

# printing a message to confirm that the data has been loaded:
print("Data loaded successfully.")

# prepare data for LSTM
# so this is assuming each time step uses 60 seconds of data
def prepare_data(data, timesteps):
 X, Y = [], []
 for i in range(len(data)-timesteps-1):
    X.append(data[i:(i+timesteps), :])
    Y.append(data[i+timesteps, 0]) # we only predicting the close price
 return np.array(X), np.array(Y)

timesteps = 60
bitstamp_X, bitstamp_y = prepare_data(bitstamp_data, timesteps)
coinbase_X, coinbase_y = prepare_data(coinbase_data, timesteps)

# splitting the data into a training set and a validation set
bitstamp_X_train, bitstamp_X_val, bitstamp_y_train, bitstamp_y_val = train_test_split(bitstamp_X, bitstamp_y, test_size=0.2)
coinbase_X_train, coinbase_X_val, coinbase_y_train, coinbase_y_val = train_test_split(coinbase_X, coinbase_y, test_size=0.2)

# creating the datasets
bitstamp_train_dataset = tf.data.Dataset.from_tensor_slices((bitstamp_X_train, bitstamp_y_train))
bitstamp_val_dataset = tf.data.Dataset.from_tensor_slices((bitstamp_X_val, bitstamp_y_val))

coinbase_train_dataset = tf.data.Dataset.from_tensor_slices((coinbase_X_train, coinbase_y_train))
coinbase_val_dataset = tf.data.Dataset.from_tensor_slices((coinbase_X_val, coinbase_y_val))

# printing a message to confirm that the datasets have been created:
print("Datasets created successfully.")

# defning LSTM model
def create_model():
    model = Sequential()
    model.add(LSTM(20, activation='tanh', input_shape=(timesteps, n)))
    model.add(Dense(1))

    # Custom Adam optimizer with a lower learning rate
    adam_optimizer = Adam(learning_rate=0.0001, clipvalue=1.0)

    # Compile the model with the custom optimizer
    model.compile(optimizer=adam_optimizer, loss='mse')

    model.summary()
    return model

# Creating and training models
bitstamp_model = create_model()
coinbase_model = create_model()

# Model training
bitstamp_history = bitstamp_model.fit(bitstamp_train_dataset.batch(256), epochs=5, validation_data=bitstamp_val_dataset.batch(256), verbose=1)
coinbase_history = coinbase_model.fit(coinbase_train_dataset.batch(256), epochs=5, validation_data=coinbase_val_dataset.batch(256), verbose=1)

# printing the training and validation loss and accuracy:
print(bitstamp_model.history.history)

# plotting the training & validation accuracy values
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(bitstamp_history.history['loss'])
plt.plot(bitstamp_history.history['val_loss'])
plt.title('Bitstamp Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# plotting the training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(coinbase_history.history['loss'], label='train')
plt.plot(coinbase_history.history['val_loss'], label='test')
plt.title('Coinbase Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()

plt.tight_layout()
plt.show()

# saving the models
bitstamp_model.save('bitstamp_model_v2.h5')
coinbase_model.save('coinbase_model_v2.h5')

# printing a message to confirm that the models have been saved!!
print("Models saved successfully!")
