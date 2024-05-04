import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('combined_stock_data.csv')

# Drop irrelevant columns
data = data.drop(columns=['Date', 'Symbol', 'Series'])

# Fill missing values if any
data = data.fillna(0)

# Standardize numerical columns
numerical_cols = ['Prev Close', 'Open', 'High', 'Low', 'Last', 'Close', 'VWAP', 'Volume', 'Turnover', 'Trades', 'Deliverable Volume', '%Deliverble']
scaler = StandardScaler()
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Save preprocessed data to a new CSV file
data.to_csv('preprocessed_combined_stock_data.csv', index=False)
