import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [1200, 1500, 1700, 1600, 1800, 2000,
              2100, 1900, 2200, 2500, 2300, 2600]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

# Draw bar chart with custom width
plt.bar(df["Month"], df["Sales"], width=0.6)

plt.title("Monthly Sales Report (Extended)", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales (in USD)", fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.6)

# Add value labels on each bar
for i, value in enumerate(df["Sales"]):
    plt.text(i, value + 20, str(value), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()