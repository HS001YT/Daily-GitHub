import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\Exam_scores.csv")

plt.figure(figsize=(8, 6))
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Create Boxplot
sns.boxplot(x="Gender", y="Exam_Score", data=data, palette="Set2")
# data.boxplot(column="Exam_Score", by="Gender", grid=False)

plt.xlabel("Gender")
plt.title("Exam Scores By Gender", fontsize=16, fontweight="bold")
plt.tight_layout()

plt.annotate("Source: ChatGPT", 
             xy=(-0.07, -0.11), xycoords="axes fraction", # Adjust xy according to need
             ha="left", fontsize=9, color="gray")

plt.get_current_fig_manager().set_window_title("Day 36")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day36.png", dpi=300, bbox_inches="tight")

plt.show()