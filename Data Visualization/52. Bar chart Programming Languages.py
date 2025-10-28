import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\programming_languages.csv")

languages = data["Language"]
popularity = data["Popularity"]

plt.figure(figsize=(10, 6), facecolor="lightgray")

bars = plt.bar(languages, popularity, color="royalblue", edgecolor="black")

# Add values on top of bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.5,
        str(bar.get_height()) + "%",
        ha="center",
        va="bottom",
        fontsize=10,
        color="black"
    )

plt.title("Programming Language Popularity", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Programming Languages", fontsize=12, labelpad=10)
plt.ylabel("Popularity (%)", fontsize=12, labelpad=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.annotate("Data Source: ChatGPT", 
             xy=(-0.1, -0.12), xycoords="axes fraction",
             ha="left", fontsize=9, color="gray")

plt.get_current_fig_manager().set_window_title("Day 52")
# plt.savefig(r"D:\Daily-GitHub\Data Visualization\other_files\Day52.png", dpi=300, bbox_inches="tight")

plt.show()
