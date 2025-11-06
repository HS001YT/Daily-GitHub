import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\heart.csv")

corr = data.corr()

plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

sns.heatmap(
    corr,
    annot=True,                  # display correlation values
    fmt=".2f",                   # format decimal places
    cmap="coolwarm",             # color scheme (from blue to red)
    linewidths=0.5,              # lines between cells
    linecolor="white",           # line color between cells
    cbar_kws={'shrink': 0.8, 'label': 'Correlation Coefficient'}  # color bar
)

plt.title("Heatmap of Feature Correlation (Heart Disease Dataset)", fontsize=18, color='darkred', pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()

plt.get_current_fig_manager().set_window_title("Day 60")
# plt.savefig(r"D:\Daily-GitHub\Data Visualization\other_files\Day60.png", dpi=300, bbox_inches="tight")

plt.show()
