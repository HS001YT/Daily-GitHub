import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files/car_prices_vs_mileage.csv")
data.set_index("Model", inplace=True)

plt.figure(figsize=(10, 6))
plt.style.use("ggplot")

plt.scatter(data.Mileage, data.Price, c='r')

plt.title("Scatter plot of Car Prices vs Mileage", \
          fontsize=16, fontweight="bold", color="navy")
plt.xlabel("Mileage", fontsize=14, fontweight="bold")
plt.ylabel("Prices", fontsize=14, fontweight="bold")

plt.get_current_fig_manager().set_window_title("Day 8")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day12.png", dpi=300, bbox_inches="tight")

plt.show()

