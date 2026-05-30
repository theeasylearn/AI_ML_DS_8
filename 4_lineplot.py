import yfinance as yf
import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt

# Fetch historical data for S&P BSE SENSEX
# Ticker symbol on Yahoo Finance is '^BSESN'
sensex = yf.Ticker("^BSESN")

# Fetch data and isolate the last 30 completed working days
df = sensex.history(period="60d") # Pulls a safe window of days
df = df.tail(30)
# print(df)
plt.figure(figsize=(14,7))
sns.lineplot(x='Date',y='Close',data=df)
plt.xticks(df.index, rotation=90)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()