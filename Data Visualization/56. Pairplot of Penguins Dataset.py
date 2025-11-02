import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset and clean missing values
data = sns.load_dataset("penguins")
data.dropna(inplace=True)

# ---------- STYLE & THEME ----------
sns.set_theme(style="darkgrid", rc={
    'axes.facecolor': 'aliceblue',        # Subplot background
    'figure.facecolor': 'lightsteelblue', # Overall figure background
    'axes.edgecolor': 'gray',             # Border color
    'grid.color': 'lightgray',            # Grid lines
    'font.family': 'Arial',
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
})

# ---------- PAIRPLOT ----------
pair = sns.pairplot(
    data,
    hue="species",              # Color by penguin species
    palette="Set2",             # Soft pastel color scheme
    diag_kind="kde",            # Smooth distribution on diagonal
    markers=["o", "s", "D"],    # Marker shapes
    plot_kws={
        'alpha': 0.8,           # Transparency
        's': 60,                # Marker size
        'edgecolor': 'black'    # Marker border color
    },
    corner=False                # Show full matrix
)

# ---------- TITLE ----------
pair.fig.suptitle("Pairplot of Penguins Dataset (Advanced Visualization)",
                  fontsize=18, fontweight='bold', color='navy')

# Adjust layout so title is visible
pair.fig.subplots_adjust(top=0.93)

# ---------- LEGEND ----------
pair._legend.set_title("Penguin Species")
for text in pair._legend.texts:
    text.set_fontsize(10)
    text.set_color("black")

# ---------- STYLE FOR EACH AXIS ----------
for ax in pair.axes.flatten():
    if ax is not None:
        ax.set_facecolor("white")  # Inside of each subplot
        ax.grid(True, color='lightgray', linewidth=0.6, alpha=0.7)
        ax.tick_params(colors="dimgray")  # Axis ticks
        ax.xaxis.label.set_color("black")
        ax.yaxis.label.set_color("black")

plt.get_current_fig_manager().set_window_title("Day 56")
# pair.fig.savefig(r"D:\Daily-GitHub\Data Visualization\other_files\Day56.png", dpi=300, bbox_inches="tight")

plt.show()