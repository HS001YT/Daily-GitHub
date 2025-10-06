import pandas as pd
import matplotlib.pyplot as plt

file_path = "D:\Daily-GitHub\Data Visualization\other_files/US_Regional_Sales_Data.csv"
df = pd.read_csv(file_path)

# Clean numeric columns
df["Unit Price"] = df["Unit Price"].astype(str).str.replace(",", "").astype(float)
df["Order Quantity"] = pd.to_numeric(df["Order Quantity"], errors="coerce")

# Calculate Sales
df["Sales"] = df["Order Quantity"] * df["Unit Price"]

# Warehouse to US Places mapping
warehouse_mapping = {
    "WARE-UHY1004": "New York",
    "WARE-NMK1003": "California",
    "WARE-PUJ1005": "Texas",
    "WARE-XYS1001": "Florida",
    "WARE-MKL1006": "Illinois",
    "WARE-NBV1002": "Washington"
}

# Replace Warhouse codes with readable names
df["WarehouseName"] = df["WarehouseCode"].map(warehouse_mapping)

# Group by Sales Channel & Warehouse
sales_data = df.groupby(["Sales Channel", "WarehouseName"])["Sales"].sum().unstack(fill_value=0)    # If found any place empty then fill it with 0

# Plot stacked bar chart
sales_data.plot(kind="bar", stacked=True, figsize=(10,6))

plt.title("Sales by Region", fontsize=16, fontweight="bold", color="navy")
plt.ylabel("Total Sales", fontweight="bold")
plt.xlabel("Sales Channel", fontweight="bold")
plt.xticks(rotation=0)
plt.legend(title="US Place", facecolor="gray")
plt.tight_layout()                                  # use this to fit the figure in the window In case if is not fitting inside it

plt.annotate("Data Source: US Regional Sales Data", 
             xy=(-0.05, -0.21), xycoords="axes fraction",
             ha="left", fontsize=9, color="gray")

plt.get_current_fig_manager().set_window_title("Day 26")
# plt.savefig("D:\Daily-GitHub\Data Visualization\other_files\Day26.png", dpi=300, bbox_inches="tight")

plt.show()