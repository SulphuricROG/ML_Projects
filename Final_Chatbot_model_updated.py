from sklearn.ensemble import RandomForestRegressor
from joblib import load
import pandas as pd
import os
import matplotlib.pyplot as plt

# Mount Google Drive
%cd /content/drive/My Drive/Chatbot/

# Define the path to the folder containing the saved models
models_folder = '/content/drive/My Drive/Chatbot/JobLib_Models/'

# Define the path to the folder containing the historical data
historical_data_folder = '/content/drive/My Drive/Chatbot/Historical_Data/'

# Define the list of stock names
stocks = [
    'ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV',
    'BAJFINANCE', 'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA',
    'DRREDDY', 'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFC', 'HEROMOTOCO',
    'HDFCBANK', 'HINDALCO', 'HINDUNILVR', 'INDUSINDBK', 'ICICIBANK', 'INFRATEL',
    'INFY', 'IOC', 'ITC', 'KOTAKBANK', 'JSWSTEEL', 'LT', 'MARUTI', 'MM', 'NESTLEIND',
    'NIFTY50_all', 'NTPC', 'ONGC', 'RELIANCE', 'POWERGRID', 'SBIN', 'SHREECEM',
    'SUNPHARMA', 'TATAMOTORS', 'TCS', 'TATASTEEL', 'TECHM', 'TITAN', 'ULTRACEMCO',
    'UPL', 'VEDL', 'WIPRO', 'ZEEL'
]

# Initialize a dictionary to store the loaded models
loaded_models = {}

# Load the models from the folder
for stock_name in stocks:
    model_path = os.path.join(models_folder, f'model_{stock_name}.joblib')
    if os.path.exists(model_path):
        loaded_model = load(model_path)
        loaded_models[stock_name] = loaded_model
    else:
        print(f"Model file {model_path} not found. Skipping {stock_name}")

# User Input and Service Selection
service = input("Select a service (1 - Closing Stock Prediction, 2 - Analysis, 3 - Information): ")

if service == '1':  # Closing Stock Prediction
    stock_name = input("Enter the stock name: ")
    if stock_name in loaded_models:
        values = {}
        for feature in ['Prev Close', 'Open', 'High', 'Low', 'Last', 'Close', 'VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume', '%Deliverble']:
            values[feature] = float(input(f"Enter the value for {feature}: "))
        new_data_df = pd.DataFrame(values, index=[0])
        predictions = loaded_models[stock_name].predict(new_data_df)
        print('Predicted Closing Price:', predictions)
    else:
        print(f"Model for {stock_name} not found.")

elif service == '2':  # Analysis
    stock_name = input("Enter the stock name for analysis: ")
    historical_data_path = os.path.join(historical_data_folder, f"{stock_name}_historical_data.csv")
    if os.path.exists(historical_data_path):
        historical_data = pd.read_csv(historical_data_path)
        closing_prices = historical_data['Close']
        dates = historical_data['Date']

        # Plot the closing price over time
        plt.figure(figsize=(12, 6))
        plt.plot(dates, closing_prices, label='Closing Price')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f"Closing Price Trend for {stock_name}")
        plt.legend()
        plt.show()

        # Plot other analysis graphs
        # 1. Plotting Volume over time
        volume = historical_data['Volume']
        plt.figure(figsize=(12, 6))
        plt.plot(dates, volume, label='Volume')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.title(f"Volume Trend for {stock_name}")
        plt.legend()
        plt.show()

        # 2. Plotting Moving Average
        window_size = 30  # Define the window size for the moving average
        rolling_avg = closing_prices.rolling(window=window_size).mean()
        plt.figure(figsize=(12, 6))
        plt.plot(dates, closing_prices, label='Closing Price')
        plt.plot(dates, rolling_avg, label=f'{window_size}-Day Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f"Moving Average Trend for {stock_name}")
        plt.legend()
        plt.show()

        # Add more analysis graphs as needed...

    else:
        print(f"Historical data file {historical_data_path} not found.")

elif service == '3':  # Information
    print("Available stocks:")
    for i, stock_name in enumerate(stocks, 1):
        print(f"{i}. {stock_name}")

    stock_name = input("Enter the stock name to get information: ")
    if stock_name in loaded_models:
        # Calculate the average values of prev_close, open, high, low, last, vwap, and volume
        avg_data = loaded_models[stock_name].feature_importances_
        print(f"Average information for {stock_name}:")
        print(f"Average Prev Close: {avg_data[0]}")
        print(f"Average Open: {avg_data[1]}")
        print(f"Average High: {avg_data[2]}")
        print(f"Average Low: {avg_data[3]}")
        print(f"Average Last: {avg_data[4]}")
        print(f"Average VWAP: {avg_data[5]}")
        print(f"Average Volume: {avg_data[6]}")
    else:
        print(f"Model for {stock_name} not found.")

else:
    print("Invalid service selection. Please select 1, 2, or 3.")
