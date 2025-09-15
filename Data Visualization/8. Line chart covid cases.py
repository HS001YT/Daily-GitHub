import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Daily-GitHub\Data Visualization\other_files\covid_cases.csv")    # I have manually made this csv file by taking data from chatgpt

# Setting 'Week' as index (makes plotting easier)
df.set_index('Week', inplace=True)

plt.figure(figsize=(14, 7))
plt.style.use("ggplot")
#plt.grid(True, linestyle='--', alpha=0.5)

plt.plot(df['Maharashtra'], label='Maharashtra')
plt.plot(df['Kerala'], label='Kerala')
plt.plot(df['Karnataka'], label='Karnataka')
plt.plot(df['Delhi'], label='Delhi')
plt.plot(df['Tamil Nadu'], label='Tamil Nadu')

plt.title("COVID-19 Active Cases Comparison from Mar-20 to Mar-21", \
          fontsize=16, fontweight="bold", color="navy")
plt.xlabel("Week Number", fontsize=14, fontweight="bold")
plt.ylabel("Active Cases", fontsize=14, fontweight="bold")

plt.legend(loc = "upper left", fontsize=12, facecolor='white', edgecolor='black')
plt.xticks(df.index, rotation=45)

plt.get_current_fig_manager().set_window_title("Day 8")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day8.png", dpi=300, bbox_inches="tight")

plt.show()
