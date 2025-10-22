import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files/study_hours.csv")
data.set_index("Student", inplace=True)

plt.figure(figsize=(10, 6))
plt.style.use("ggplot")

plt.scatter(data["Study Hours"], data.Marks, c='r')

plt.title("Scatter plot of Hours vs Marks", \
          fontsize=16, fontweight="bold", color="navy")
plt.xlabel("Hours", fontsize=14, fontweight="bold")
plt.ylabel("Marks", fontsize=14, fontweight="bold")
plt.tight_layout()

plt.get_current_fig_manager().set_window_title("Day 44")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day44.png", dpi=300, bbox_inches="tight")

plt.show()