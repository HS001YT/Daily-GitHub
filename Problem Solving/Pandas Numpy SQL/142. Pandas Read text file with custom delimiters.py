import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "Other Files", "data.txt")

# 1. Read text file with custom delimiters
df = pd.read_csv(
    file_path,
    sep=r"[|,;]",      # custom delimiters
    engine="python"
)

# 2. Show first few rows
print(df.head())

# 3. Remove extra spaces from column names
df.columns = df.columns.str.strip()

# 4. Remove extra spaces from data
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

# 5. Remove duplicate rows
df = df.drop_duplicates()

# 6. Convert column types
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 7. Replace missing values
df["Amount"] = df["Amount"].fillna(0)

# 8. Filter data
df = df[df["Amount"] > 0]

# 9. Group and summarize
summary = df.groupby("Category")["Amount"].sum()

# 10. Save result
summary.to_csv(os.path.join(current_dir, "Other Files", "summary_output.csv"))

print(summary)