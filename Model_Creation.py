from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from joblib import dump
import pandas as pd

# Load the dataset
data = pd.read_csv('combined_stock_data.csv')

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

# Initialize a dictionary to store the models
models = {}

for stock_name in stocks:
    # Filter the dataset for the current stock
    stock_data = data[data['Stock'] == stock_name]

    # Check if the dataset has enough samples
    if len(stock_data) < 2:
        print(f"Skipping {stock_name} due to insufficient data")
        continue

    # Define features and target variable
    X = stock_data[['Prev Close', 'Open', 'High', 'Low', 'Last', 'Close', 'VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume', '%Deliverble']]
    y = stock_data['Close']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Handle missing values in the features
    imputer = SimpleImputer(strategy='mean')
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    # Initialize and train the model
    model = RandomForestRegressor()
    model.fit(X_train_imputed, y_train)

    # Store the model for the current stock
    models[stock_name] = model

    # Save the model to a file
    dump(model, f'{stock_name}_random_forest_model.joblib')

    # Make predictions
    y_pred = model.predict(X_test_imputed)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error for {stock_name}: {mse}')

# You can now use the models dictionary to make predictions for each stock
