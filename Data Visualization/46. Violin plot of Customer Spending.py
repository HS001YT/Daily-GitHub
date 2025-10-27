import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\customer_data.csv")

# ------------------ GLOBAL STYLE ------------------
sns.set_style("whitegrid")       # whitegrid, darkgrid, white, dark, ticks
sns.set_palette("pastel")        # deep, muted, bright, dark, colorblind

# ------------------ PLOT 1: Spending by Gender ------------------
plt.figure(figsize=(10, 6), facecolor="lightgray")
ax = sns.violinplot(
    x="gender",
    y="spending",
    data=data,
    palette="Set2",
    inner="quartile",
    linewidth=1.2,
    saturation=0.8,
    bw=0.3,
    cut=0,
    scale="count",
    orient="v",
    width=0.7,
    dodge=True
)

plt.title("Customer Spending by Gender", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Gender", fontsize=12, labelpad=10)
plt.ylabel("Spending", fontsize=12, labelpad=10)
plt.xticks(rotation=0, fontsize=11)
plt.yticks(fontsize=11)


# I have tried some new functions

# Text and annotation
plt.text(-0.4, 22000, "High spending pattern for Males", fontsize=10, color="red")
plt.annotate("Testing new things",
             xy=(1, 21000), xytext=(0.7, 23000),
             arrowprops=dict(arrowstyle="->", color="black"),
             fontsize=10, color="black")

# plt.grid(axis="y", linestyle="--", alpha=0.7)
# sns.despine(left=True, bottom=True)

plt.legend(title="By Gender", loc="upper right", fontsize=10, title_fontsize=11)
plt.get_current_fig_manager().set_window_title("Customer Spending Violin Plot")

plt.annotate("Data Source: Kaggle Customer Spending Dataset",
             xy=(-0.1, -0.12), xycoords="axes fraction",
             ha="left", fontsize=9, color="gray")

plt.tight_layout()
# plt.savefig(r"D:\Daily-GitHub\Data Visualization\other_files\Day 46.1.png", dpi=300, bbox_inches="tight")
plt.show()

# ------------------ PLOT 2: Spending by Education (with Gender Split) ------------------
plt.figure(figsize=(10, 6), facecolor="lightgray")
ax2 = sns.violinplot(
    x="education",
    y="spending",
    hue="gender",
    data=data,
    split=True,
    palette="coolwarm",
    inner="quartile",
    linewidth=1.2
)

ax2.set_facecolor("#f8f9fa")
plt.title("Customer Spending by Education Level and Gender", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Education Level", fontsize=12, labelpad=10, fontweight="bold")
plt.ylabel("Spending", fontsize=12, labelpad=10, fontweight="bold")
plt.xticks(rotation=0, fontsize=11)
plt.yticks(fontsize=11)

plt.legend(title="Gender", loc="upper left", fontsize=10, title_fontsize=11)
plt.annotate("Data Source: Kaggle Customer Spending Dataset",
             xy=(-0.1, -0.15), xycoords="axes fraction",
             ha="left", fontsize=9, color="gray")

plt.tight_layout()
# plt.savefig(r"D:\Daily-GitHub\Data Visualization\other_files\Day 46.2.png", dpi=300, bbox_inches="tight")
plt.show()