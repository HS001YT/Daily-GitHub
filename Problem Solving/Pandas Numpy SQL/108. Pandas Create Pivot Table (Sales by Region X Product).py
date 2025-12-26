import pandas as pd

# -----------------------------
# Sample Sales Dataset
# -----------------------------
data = {
    "Region": ["North", "North", "South", "South", "East", "East", "West", "West"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Laptop", "Phone", "Laptop", "Phone"],
    "Sales": [1000, 800, 900, 700, 1100, 600, 950, 650],
    "Quantity": [5, 8, 6, 7, 7, 5, 6, 6],
    "Salesperson": ["A", "B", "A", "C", "B", "C", "A", "B"]
}

df = pd.DataFrame(data)

# -----------------------------
# Pivot Table
# -----------------------------
pivot_table = pd.pivot_table(
    df,
    values=["Sales", "Quantity"],
    index="Region",
    columns="Product",
    aggfunc={
        "Sales": ["sum", "mean", "max"],
        "Quantity": "sum"
    },
    fill_value=0
)

# -----------------------------
# Name Column Levels (IMPORTANT)
# -----------------------------
pivot_table.columns.names = ["Metric", "Aggregation", "Product"]

# -----------------------------
# Add Grand Total Row
# -----------------------------
pivot_table.loc["Grand Total"] = pivot_table.sum()

# -----------------------------
# Sorting & Rounding
# -----------------------------
pivot_table = pivot_table.round(2)

print(pivot_table)
