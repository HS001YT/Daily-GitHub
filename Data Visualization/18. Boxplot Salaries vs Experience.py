import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\Salary_Data.csv")

# Create Boxplot
plt.figure(figsize=(8, 6))
plt.grid(axis="y", linestyle="--", alpha=0.7)
sns.boxplot(x=pd.cut(df["YearsExperience"], bins=[0,2,5,10,20]), y="Salary", data=df, palette="Set2")

plt.xlabel("Years of Experience")
plt.title("Salaries vs Experience", fontsize=16, fontweight="bold")

plt.annotate("Source: ChatGPT", 
             xy=(-0.1, -0.13), xycoords="axes fraction", # Adjust xy according to need
             ha="left", fontsize=9, color="gray")

plt.get_current_fig_manager().set_window_title("Day 18")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day18.png", dpi=300, bbox_inches="tight")
plt.show()
