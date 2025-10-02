import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files/temperatures.csv")    
# I have manually made this csv file by taking data from chatgpt

# Setting 'Day' as index (makes plotting easier)
df.set_index('Day', inplace=True)

plt.figure(figsize=(14, 7))
plt.style.use("ggplot")
#plt.grid(True, linestyle='--', alpha=0.5)

plt.plot(df['Temperature'])

plt.title("Daily Temperatures", \
          fontsize=16, fontweight="bold", color="navy")
plt.xlabel("Week Days", fontsize=14, fontweight="bold")
plt.ylabel("Temperature", fontsize=14, fontweight="bold")

# plt.xticks(df.index, rotation=45)

plt.get_current_fig_manager().set_window_title("Day 22")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day22.png", dpi=300, bbox_inches="tight")

plt.show()
