import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\social_media_usage.csv")

# Prepare data
platforms = data["Platform"]
users = data["Users"]

plt.figure(figsize=(8, 6), facecolor="lightgray")

# Create pie chart
colors = plt.cm.Set3.colors  # predefined color palette
explode = [0.05] * len(platforms)  # separate all slices slightly

wedges, texts, autotexts = plt.pie(
    users,
    labels=platforms,
    autopct="%1.1f%%",      # show % values
    startangle=90,          # rotate start position
    colors=colors,
    explode=explode,
    shadow=True,
    textprops={"fontsize": 10, "color": "black"},
)

# Customize title and legend
plt.title("Social Media Usage Distribution", fontsize=16, fontweight="bold", pad=20)
plt.legend(platforms, title="Platforms", loc="upper right", bbox_to_anchor=(1.3, 1))

# Add annotation
plt.annotate("Data Source: ChatGPT", xy=(0, 0), xycoords="axes fraction",
             ha="center", fontsize=9, color="gray")

# Set window title
plt.get_current_fig_manager().set_window_title("Day 50")

# plt.savefig(r"D:\Daily-GitHub\Data Visualization\other_files\Day50.png", dpi=300, bbox_inches="tight")

plt.show()
