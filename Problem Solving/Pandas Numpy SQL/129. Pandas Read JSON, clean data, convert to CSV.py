# 1. IMPORTING FILES
import pandas as pd
import numpy as np
import json
from datetime import datetime



# 2. LOAD JSON DATA
def load_json_file(file_path):
    """Read JSON file"""
    return pd.read_json(file_path)

def load_json_string():
    """JSON from API / raw string"""
    raw_json = """
    [
        {"id": 1, "name": "Alice", "age": 22, "salary": "45000", "city": "Delhi", "joined": "2023-01-10"},
        {"id": 2, "name": "Bob", "age": null, "salary": "50000", "city": "Mumbai", "joined": "2022-12-01"},
        {"id": 3, "name": "Charlie", "age": 24, "salary": null, "city": "Delhi", "joined": "2023-03-15"},
        {"id": 4, "name": "David", "age": 21, "salary": "42000", "city": null, "joined": "2023-06-20"},
        {"id": 5, "name": "Eve", "age": 23, "salary": "48000", "city": "Bangalore", "joined": "invalid_date"}
    ]
    """
    return pd.read_json(raw_json)

df = load_json_string()



# 3. BASIC INSPECTION
print("\n--- BASIC INFO ---")
print(df.head())
print(df.info())
print(df.describe(include="all"))



# 4. DATA CLEANING

# Rename columns
df.rename(columns={"joined": "joining_date"}, inplace=True)

# Trim whitespace
df["name"] = df["name"].str.strip()

# Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["city"] = df["city"].fillna("Unknown")

# Convert salary to numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Fill missing salary with mean
df["salary"].fillna(df["salary"].mean(), inplace=True)

# Convert date column
df["joining_date"] = pd.to_datetime(df["joining_date"], errors="coerce")

# Drop rows with invalid dates
df.dropna(subset=["joining_date"], inplace=True)



# 5. FEATURE ENGINEERING

# Salary category
df["salary_level"] = pd.cut(
    df["salary"],
    bins=[0, 45000, 50000, 100000],
    labels=["Low", "Medium", "High"]
)

# Experience in days
df["experience_days"] = (pd.Timestamp.now() - df["joining_date"]).dt.days

# Uppercase names
df["name_upper"] = df["name"].str.upper()



# 6. FILTERING & SORTING

high_salary_df = df[df["salary"] > 46000]
sorted_df = df.sort_values(by="salary", ascending=False)



# 7. GROUPBY & AGGREGATION

city_salary_summary = (
    df.groupby("city")
      .agg(
          employee_count=("id", "count"),
          avg_salary=("salary", "mean"),
          max_salary=("salary", "max")
      )
      .reset_index()
)

print("\n--- CITY SALARY SUMMARY ---")
print(city_salary_summary)



# 8. DATA VALIDATION

assert df["age"].min() > 0, "Invalid age detected"
assert df["salary"].min() > 0, "Invalid salary detected"



# 9. ADVANCED OPERATIONS

# Apply custom function
def bonus_calculation(salary):
    return salary * 0.10

df["annual_bonus"] = df["salary"].apply(bonus_calculation)

# Vectorized condition
df["is_senior"] = np.where(df["experience_days"] > 365, "Yes", "No")

# Duplicate check
df.drop_duplicates(subset=["id"], inplace=True)



# 10. EXPORT TO CSV

df.to_csv("Problem Solving/Pandas Numpy SQL/Other Files/129cleaned_data.csv", index=False)
city_salary_summary.to_csv("Problem Solving/Pandas Numpy SQL/Other Files/129city_salary_summary.csv", index=False)



# 11. OPTIONAL: PIPELINE STYLE

cleaned_pipeline = (
    df.assign(
        salary_lakh=lambda x: x["salary"] / 100000
    )
    .query("salary_lakh > 0.4")
    .sort_values("salary_lakh", ascending=False)
)

print("\n--- PIPELINE RESULT ---")
print(cleaned_pipeline)