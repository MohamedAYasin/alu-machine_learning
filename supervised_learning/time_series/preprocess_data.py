#!/usr/bin/env python3
#!/usr/bin/env python3

import os
import zipfile
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# paths to zipped files
bitstamp_zip = 'supervised_learning/time_series/data_files/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv.zip'
coinbase_zip = 'supervised_learning/time_series/data_files/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip'

# unziping the file
with zipfile.ZipFile(bitstamp_zip, 'r') as zip_ref:
    zip_ref.extractall('supervised_learning/time_series/data_files')
with zipfile.ZipFile(coinbase_zip, 'r') as zip_ref:
    zip_ref.extractall('supervised_learning/time_series/data_files')

# loading data
bitstamp_raw_data = pd.read_csv('supervised_learning/time_series/data_files/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv')
coinbase_raw_data = pd.read_csv('supervised_learning/time_series/data_files/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv')

# checking if loaded correctly
print("Bitstamp Data Loaded:")
print(bitstamp_raw_data.head())
print("Shape:", bitstamp_raw_data.shape)
print("\nCoinbase Data Loaded:")
print(coinbase_raw_data.head())
print("Shape:", coinbase_raw_data.shape)

# dropping NaN values
bitstamp_raw_data = bitstamp_raw_data.dropna()
coinbase_raw_data = coinbase_raw_data.dropna()
# checking if dropped correctly
print("NaN Values Dropped Correctly.")

def preprocess_data(df, filename):
   # drop rows with NaN values
   df = df.dropna(subset=['Close'])

   # select the column to predict
   data_to_use = df['Close'].values

   # reshape the data
   data_to_use = np.reshape(data_to_use, (-1, 1))

   # normalize the data
   scaler = MinMaxScaler()
   data_to_use = scaler.fit_transform(data_to_use)

   # save preprocessed data to a file
   np.save(filename, data_to_use)

# preprocess data
preprocess_data(bitstamp_raw_data, 'bitstamp_preprocessed_data_v2.npy')
preprocess_data(coinbase_raw_data, 'coinbase_preprocessed_data_v2.npy')

# Load preprocessed data
bitstamp_preprocessed_data_v2 = np.load('bitstamp_preprocessed_data_v2.npy')
coinbase_preprocessed_data_v2 = np.load('coinbase_preprocessed_data_v2.npy')

# Check for NaN values in the preprocessed data
print("Checking for NaN values in preprocessed data...")
print("Bitstamp preprocessed data has NaN values:", np.isnan(bitstamp_preprocessed_data_v2).any())
print("Coinbase preprocessed data has NaN values:", np.isnan(coinbase_preprocessed_data_v2).any())

# Print preprocessed data
print(bitstamp_preprocessed_data_v2)
print(coinbase_preprocessed_data_v2)
