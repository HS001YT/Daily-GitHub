import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files/marks.csv")

subjects = ["English", "Physics", "Chemistry", "Math", "Hindi"]

# Extract values directly as a 2D array
array = data[subjects].T.values   # transpose so subjects go along rows

sns.heatmap(array, cmap="GnBu", alpha=0.9, cbar=False,          # cmap changes the theme
            linecolor="Black", linewidths=1, annot=True,
            xticklabels=data["Name"], yticklabels=subjects)

plt.xlabel("Names")
plt.ylabel("Marks in Subjects")

plt.title("Marks in different Subject", fontsize=16, fontweight="bold")
plt.get_current_fig_manager().set_window_title("Day 10")

# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day10.png", dpi=300, bbox_inches="tight")
plt.show()
