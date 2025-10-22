import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\website_traffic.csv")

# Set Month as index
data.set_index("Month", inplace=True)

# Plot stacked area chart
plt.figure(figsize=(10, 6))
plt.stackplot(data.index, 
              data["Organic"], data["Social"], data["Direct"], data["Referral"], 
              labels=["Organic", "Social", "Direct", "Referral"], 
              alpha=0.9)

# Chart formatting
plt.title("Website Traffic Sources Over Months", fontsize=16, weight='bold', pad=20)
plt.xlabel("Month", fontsize=12, weight='bold')
plt.ylabel("Number of Visitors", fontsize=12, weight='bold')
plt.legend(title="Traffic Source", loc="upper left", fontsize=12, facecolor='lightgray', edgecolor='black')
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.get_current_fig_manager().set_window_title("Day 42")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day42.png", dpi=300, bbox_inches="tight")

plt.show()
