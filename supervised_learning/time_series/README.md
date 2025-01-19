# Time Series Forecasting for Bitcoin Prices

This project demonstrates a simple and effective approach to forecasting Bitcoin prices using time series forecasting. The methods and implementation in this project are based on Python and TensorFlow.

## Folder Contents

### Files in this folder:
- **`Time_Series.ipynb`**:  
  A Jupyter Notebook containing the complete workflow for forecasting Bitcoin prices using time series data. This includes:
  - Data preprocessing.
  - Dataset creation.
  - Model training and evaluation.
  - Visualization of the results.

- **`forecast_btc.py`**:  
  A Python script version of the forecasting workflow for ease of execution. Use this file to train and evaluate the forecasting model without requiring Jupyter Notebook.

- **`preprocess_data.py`**:  
  This script handles data preprocessing for the time series model. It includes:
  - Loading raw data.
  - Formatting the data into sequences.
  - Normalizing and preparing data for training.

- **`README.md`**:  
  The current file, providing an overview of the project and its components.

---

## Methodology
1. **Data Preprocessing**:  
   The data was cleaned, normalized, and prepared as sliding windows to enable sequential model training.

2. **Model Architecture**:  
   - A TensorFlow-based Recurrent Neural Network (RNN) model was used.
   - Layers include LSTM cells, Dropout, and Dense layers for prediction.
   - The architecture is designed to handle sequential dependencies effectively.

3. **Performance**:  
   - The model's performance was evaluated using Mean Absolute Error (MAE) and visualized predictions vs. actual values. See the detailed results in the linked article below.

---

## Instructions to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/MohamedAYasin/alu-machine_learning.git
   ```
2. Navigate to the `time_series` directory:
   ```bash
   cd supervised_learning/time_series
   ```
3. To execute the Python script:
   ```bash
   python forecast_btc.py
   ```

4. Alternatively, open the Jupyter Notebook `Time_Series.ipynb` to interact with the code step by step.

---

## Article Link
For a detailed explanation of the methodology and results, read the accompanying post I published on Medium:  
[Making Money with BTC Using Time Series Forecasting](https://medium.com/@m.yasin/making-money-with-btc-using-time-series-forecasting-a-simple-guide-902adf08a235)

---

Feel free to explore, contribute, or raise any issues! 🚀

--- 

Thank you!
