import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\countries_population.csv")
country = data.Country
population = data.Population

plt.pie(population, labels = country, radius = 1.1, \
        autopct = "%0.1f%%", explode=[0.1,0,0.1,0,0],\
        startangle=90, shadow = True)
plt.title("Top 5 Countries by Populaiton", fontsize=14, fontweight="bold", color="navy")

# Uncomment to see the Total population of 5 countries
# total = population.sum()
# plt.figtext(0.5, 0.01, f"Total = {total}", ha="center", fontsize=10)

plt.get_current_fig_manager().set_window_title("Day 20")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day20.png", dpi=300, bbox_inches="tight")

plt.show()