import pandas as pd
# pip install mplfinance  
import mplfinance as mpl 

#load file
df = pd.read_csv('nifty50.csv').squeeze()
# print(df)

#create another dataframe 
stock = pd.DataFrame({
    'dates': pd.to_datetime(df['Date']),
    'open': df['Open'],
    'close': df['Close'],
    'high' : df['High'],
    'low' : df['Low'],
});
print(stock)
stock.set_index('dates',inplace=True)
mpl.plot(stock,style='yahoo',type='candle')
mpl.show()