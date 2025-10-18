import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\monthly_rainfall.csv")
data.set_index("Month", inplace=True)

plt.figure(figsize=(10,6))
plt.style.use("ggplot")
plt.plot(data.index, data['Rainfall'])

plt.title("Monthly Rainfall", fontsize=16, fontweight="bold", color="purple")
plt.xlabel("Months", fontsize = 14)
plt.ylabel("Rainfall", fontsize = 14)
plt.tight_layout()

plt.get_current_fig_manager().set_window_title("Day 32")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day32.png", dpi=300, bbox_inches="tight")

plt.show()