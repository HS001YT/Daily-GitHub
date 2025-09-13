import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\expenses.csv")
category = data.Category
amount = data.Amount

plt.pie(amount, labels = category, radius = 1.1, \
        autopct = "%0.1f%%", explode=[0,0.1,0,0,0,0.15],\
        startangle=90, shadow = True)
plt.title("Monthly Expenses", fontsize=14, fontweight="bold", color="navy")

total = amount.sum()
plt.figtext(0.5, 0.01, f"Total = {total}", ha="center", fontsize=10)

plt.get_current_fig_manager().set_window_title("Day 6")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day6.png", dpi=300, bbox_inches="tight")

plt.show()