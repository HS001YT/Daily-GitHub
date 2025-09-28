import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Correlation matrix
corr = df.corr()
# .corr() - This is a pandas DataFrame method that calculates the correlation coefficients between all pairs of numeric columns. By default, it uses Pearson's correlation.

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, linecolor="White", linewidths=1, cmap='coolwarm', fmt=".2f")

plt.title("Correlation of Iris Dataset", fontsize=16, fontweight="bold", color="magenta")
plt.get_current_fig_manager().set_window_title("Day 16")

# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day16.png", dpi=300, bbox_inches="tight")
plt.show()
