import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\company_revenue.csv")

# Create interactive treemap
fig = px.treemap(
    data,
    path=["Company", "Department"],   # Hierarchy levels
    values="Revenue",                 # Size of each block
    color="Revenue",                  # Color intensity based on revenue
    color_continuous_scale="Tealgrn", # Color scheme (you can use 'Viridis', 'Blues', 'Aggrnyl', etc.)
    title="Company Revenue Treemap",
)

# Update layout for better visuals
fig.update_layout(
    title_font=dict(size=22, family="Arial", color="darkblue"),
    paper_bgcolor="whitesmoke",
    plot_bgcolor="whitesmoke",
    margin=dict(t=60, l=0, r=0, b=0)
)

plt.get_current_fig_manager().set_window_title("Day 58")
# fig.write_image(r"D:\Daily-GitHub\Data Visualization\other_files\Day58.png", scale=2)

fig.show()