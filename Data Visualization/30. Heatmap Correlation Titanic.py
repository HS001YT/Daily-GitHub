import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

df = titanic.select_dtypes(include=['number'])
df = df.dropna(how="all")
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, linecolor="white", linewidths=1, cmap='coolwarm', fmt=".2f", square=True)

plt.title("Correlation Heatmap of Titanic Dataset", fontsize=16, fontweight="bold", color="purple")
plt.get_current_fig_manager().set_window_title("Day 30")

# plt.savefig(r"D:\Daily-GitHub\Data Visualization/other_files\Day30.png", dpi=300, bbox_inches="tight")
plt.show()