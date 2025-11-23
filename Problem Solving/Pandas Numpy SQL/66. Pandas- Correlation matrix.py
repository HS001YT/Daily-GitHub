import pandas as pd

# Modified sample data
data = {
    'Age': [22, 25, 28, 35, 40, 45, 50],
    'Salary': [25000, 30000, 40000, 60000, 65000, 70000, 80000],
    'Experience': [1, 3, 5, 7, 9, 10, 15],
    'Score': [70, 75, 80, 85, 83, 79, 77],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT']
}

df = pd.DataFrame(data)

# Calculate correlation matrix (numeric columns only)
corr_matrix = df.corr(
    method='pearson',        # Options: 'pearson', 'kendall', 'spearman'
    min_periods=1,           # Minimum valid observations required per pair
    numeric_only=True        # Include only numeric columns
)

print("Correlation Matrix:\n")
print(corr_matrix)