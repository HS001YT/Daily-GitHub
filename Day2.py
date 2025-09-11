import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
deliveries = pd.read_csv("D:\Daily-GitHub\other_files\deliveries.csv")

# Calculate Total runs per team
team_runs = deliveries.groupby("batting_team")["total_runs"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))

# Vertical Bar Chart
# bars = plt.bar(team_runs.index, team_runs.values, color="orange", edgecolor="black")
# for bar in bars:
#     plt.text(bar.get_x() + bar.get_width()/2, 
#              bar.get_height(), 
#              str(bar.get_height()), 
#              ha="center", va="bottom", fontsize=10, rotation=90)

# Horizontal Bar Chart
bars = plt.barh(team_runs.index, team_runs.values, color="seagreen")
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2,
            str(bar.get_width()), va="center", fontsize=10)    
    
plt.title("Total Runs Scored by IPL Teams", fontsize=16, fontweight="bold")
plt.xlabel("Teams")
plt.ylabel("Total Runs")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Background text
plt.annotate("Data Source: Kaggle IPL Dataset", 
             xy=(-0.3, -0.13), xycoords="axes fraction", # Adjust xy according to need
             ha="left", fontsize=9, color="gray")

# Change window title
plt.get_current_fig_manager().set_window_title("Day 2")

plt.savefig("other_files\Day2.png", dpi=300, bbox_inches="tight")
plt.show()

# Day2.png is also uploaded in the other_files folder. You can also check that.