import matplotlib.pyplot as plt
import pandas as pd;
import seaborn as sns

# Load Titanic dataset
data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\USA Housing Dataset.csv")
data = data[data["price"] < 2_000_000]

plt.figure(figsize=(8, 6))
plt.grid(axis="y", linestyle="--", alpha=0.7)

sns.histplot(data=data, x="price", bins=20, kde=True, color="skyblue") # Remove element to see normal histogram view
plt.title("House Prices", fontsize=16, fontweight="bold")
plt.xlabel("Prices", fontweight="bold")
plt.ylabel("Numbers", fontweight="bold")
plt.tight_layout()

plt.annotate("Source: Kaggle", 
             xy=(0.01, 0.03), xycoords="figure fraction",
             ha="left", fontsize=9, color="gray")

plt.get_current_fig_manager().set_window_title("Day 38")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day38.png", dpi=300, bbox_inches="tight")

plt.show()