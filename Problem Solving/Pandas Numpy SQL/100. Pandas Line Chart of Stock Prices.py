import pandas as pd
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "Other Files", "stocks.csv")

df = pd.read_csv(file_path)

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

df['MA_3'] = df['Close'].rolling(window=3).mean()
df['MA_5'] = df['Close'].rolling(window=5).mean()

plt.figure()
plt.plot(df.index, df['Close'], label='Close Price')
plt.plot(df.index, df['MA_3'], linestyle='--', label='3-Day MA')
plt.plot(df.index, df['MA_5'], linestyle=':', label='5-Day MA')

plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Price with Moving Averages")
plt.get_current_fig_manager().set_window_title("Day 100")

plt.legend()
plt.grid(True)
plt.xticks(rotation=45, ha='right')

plt.show()