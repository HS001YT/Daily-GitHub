import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\smartphone_market_share.csv")

# Set clean style
sns.set(style="whitegrid")

# Plot Donut Chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    data["Market_Share"],
    labels=data["Brand"],
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={'width': 0.35, 'edgecolor': 'white'},
    textprops={'fontsize': 12, 'color': 'black'}
)

# 💡 Adjust label and percentage positions
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)
    # Moves percentage slightly outward
    autotext.set_position((autotext.get_position()[0]*1.3,
                           autotext.get_position()[1]*1.3))

# Add white circle for donut effect
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Title
plt.title("Smartphone Market Share", fontsize=16, weight='bold', pad=20)
plt.get_current_fig_manager().set_window_title("Day 34")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day34.png", dpi=300, bbox_inches="tight")

plt.tight_layout()
plt.show()
