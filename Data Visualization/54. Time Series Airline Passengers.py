import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Daily-GitHub\Data Visualization\other_files\airline_passengers.csv")
data['Month'] = pd.to_datetime(data['Month'])
data['Month'] = data['Month'].dt.strftime('%b %Y')

styles = {
    "Air India":  {"dash": "solid", "symbol": "circle"},
    "IndiGo":     {"dash": "dash",  "symbol": "square"},
    "SpiceJet":   {"dash": "dot",   "symbol": "diamond"},
}

# Create the figure
fig = go.Figure()

for airline, style in styles.items():
    subset = data[data["Airline"] == airline]
    fig.add_trace(go.Scatter(
        x=subset["Month"],
        y=subset["Passengers"],
        mode="lines+markers",
        name=airline,
        line=dict(dash=style["dash"], width=2.5),
        marker=dict(symbol=style["symbol"], size=8),
    ))

# Apply layout and background styling
fig.update_layout(
    title="Monthly Airline Passengers (2024)",
    xaxis_title="Month",
    yaxis_title="Number of Passengers",
    title_font=dict(size=22, family="Arial Black", color="#1E3D59"),
    legend_title="Airline Company",
    hovermode="x unified",

    # --- Modern light theme background ---
    plot_bgcolor="rgba(240,248,255,1)",   # soft blue background for chart area
    paper_bgcolor="rgba(230,240,250,1)",  # slightly darker frame background

    # --- Axis and grid styling ---
    xaxis=dict(showgrid=True, gridcolor="lightgray", gridwidth=0.5, zeroline=False),
    yaxis=dict(showgrid=True, gridcolor="lightgray", gridwidth=0.5, zeroline=False),

    # --- Legend ---
    legend=dict(
        bgcolor="rgba(255,255,255,0.7)",
        bordercolor="lightgray",
        borderwidth=1,
        font=dict(size=11)
    )
)

fig.add_annotation(
    text="Data Source: ChatGPT",
    xref="paper", yref="paper",
    x=0, y=-0.18,
    showarrow=False,
    font=dict(size=11, color="gray")
)

fig.show()

# fig.write_image(r"D:\Daily-GitHub\Data Visualization\other_files\Day54.png", scale=3)