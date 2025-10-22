import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\WineQT.csv")
data.set_index("Id", inplace=True)

df = data.select_dtypes(include=['number'])
df = df.dropna(how="all")
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, linecolor="white", linewidths=1, cbar=False, cmap='coolwarm', fmt=".2f", square=True)

plt.tight_layout()
plt.title("Correlation Heatmap of Wine Quality", fontsize=16, fontweight="bold", color="purple")

plt.get_current_fig_manager().set_window_title("Day 40")
# plt.savefig(r"D:\Daily-GitHub\Data Visualization/other_files\Day40.png", dpi=300, bbox_inches="tight")

plt.show()