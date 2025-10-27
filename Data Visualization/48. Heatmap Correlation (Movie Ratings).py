import pandas as pd
import plotly.express as px
import plotly.io as pio

# Read your CSV file
data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\TMDB_MovieDateset.csv")

# Compute correlation for numeric columns only
corr = data.corr(numeric_only=True)

# Create interactive heatmap
fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    zmin=-1, zmax=1
)

# Customize layout (like window title & look)
fig.update_layout(
    width=800,
    height=600,
    title_font=dict(size=20, family="Arial", color="black"),
    xaxis_title="Features",
    yaxis_title="Features",
    template="plotly_white"
)

# ---------- Change window/tab title ----------
fig.update_layout(title_text="Interactive Correlation Heatmap (Movie Dataset)")

# ---------- Save as image ----------
# pio.write_image(fig, r"D:\Daily-GitHub\Data Visualization\other_files\Day48.png", scale=3)

fig.show()