import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf

start = dt.datetime(2024, 1, 1)     # (YYYY, MM, DD)
end = dt.datetime(2025, 9, 10)

# We can choose graph data from these - ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

tesla = yf.download("TSLA", start, end)[["Close"]]  # By Specifying the data we require we can fast the process
google = yf.download("GOOG", start, end)[["Close"]]

plt.figure(figsize=(10, 6))

# Two Grid style
style.use("ggplot")
# plt.grid(color = "black", linestyle = "--", linewidth = 1)

plt.plot(tesla["Close"], label="Tesla")         # ["Close"] is used here for better legend
plt.plot(google["Close"], label="Google")

plt.title("Comparison Chart")
plt.legend(loc = "lower right")
plt.xlabel("Months", fontsize = 15)
plt.ylabel("Stock Prices", fontsize = 15)

plt.get_current_fig_manager().set_window_title("Day 4")
plt.savefig("other_files\Day4.1.png", dpi=300, bbox_inches="tight")

plt.show()