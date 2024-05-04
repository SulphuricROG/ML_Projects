import pandas as pd
import glob

# List of all CSV files
csv_files = [
    'ADANIPORTS.csv', 'ASIANPAINT.csv', 'AXISBANK.csv', 'BAJAJ-AUTO.csv', 'BAJAJFINSV.csv',
    'BAJFINANCE.csv', 'BHARTIARTL.csv', 'BPCL.csv', 'BRITANNIA.csv', 'CIPLA.csv', 'COALINDIA.csv',
    'DRREDDY.csv', 'EICHERMOT.csv', 'GAIL.csv', 'GRASIM.csv', 'HCLTECH.csv', 'HDFC.csv',
    'HEROMOTOCO.csv', 'HDFCBANK.csv', 'HINDALCO.csv', 'HINDUNILVR.csv', 'INDUSINDBK.csv',
    'ICICIBANK.csv', 'INFRATEL.csv', 'INFY.csv', 'IOC.csv', 'ITC.csv', 'KOTAKBANK.csv',
    'JSWSTEEL.csv', 'LT.csv', 'MARUTI.csv', 'MM.csv', 'NESTLEIND.csv', 'NIFTY50_all.csv',
    'NTPC.csv', 'ONGC.csv', 'RELIANCE.csv', 'POWERGRID.csv', 'SBIN.csv', 'SHREECEM.csv',
    'SUNPHARMA.csv', 'TATAMOTORS.csv', 'TCS.csv', 'TATASTEEL.csv', 'TECHM.csv', 'TITAN.csv',
    'ULTRACEMCO.csv', 'UPL.csv', 'VEDL.csv', 'WIPRO.csv', 'ZEEL.csv'
]

# Load individual datasets for each stock
dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    df['Stock'] = file.split('.')[0]  # Add a column to identify each stock
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined dataset to a new CSV file
combined_df.to_csv('combined_stock_data.csv', index=False)
