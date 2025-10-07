# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\gold_monthly_csv.csv")

# # Convert 'Date' to datetime format (monthly)
# data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')

# # Set 'Date' as the index
# data.set_index("Date", inplace = True)

# plt.figure(figsize=(10,6))
# plt.style.use("ggplot")

# data.Price.plot()

# # Format x-axis to show every year
# ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.YearLocator())   # Tick every year
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format as YYYY
# plt.xticks(rotation=45)  # Rotate labels so they don't overlap

# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read CSV
data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization/other_files/gold_monthly_csv.csv")

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')

# Set 'Date' as index
data.set_index('Date', inplace=True)

# Plot
plt.figure(figsize=(10,6))
plt.style.use("ggplot")
plt.plot(data.index, data['Price'])

# Format x-axis to show every 3 years
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator(3))  # Tick every 3 years
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)

plt.xlabel("Year")
plt.ylabel("Gold Price (USD per ounce)")
plt.title("Monthly Gold Price Over Time")
plt.tight_layout()  # Prevent labels from getting cut off

plt.get_current_fig_manager().set_window_title("Day 28")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day28.png", dpi=300, bbox_inches="tight")

plt.show()
