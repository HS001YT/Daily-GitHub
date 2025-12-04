import pandas as pd

data = {'region': ['North', 'South', 'North', 'East', 'South', 'North', 'East'],
    'year': [2021, 2021, 2022, 2022, 2022, 2021, 2021],
    'sales': [100, 150, 200, 130, 170, 120, 110]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#   region  year  sales
# 0  North  2021    100
# 1  South  2021    150
# 2  North  2022    200
# 3   East  2022    130
# 4  South  2022    170
# 5  North  2021    120
# 6   East  2021    110


# Group by region and year, summing sales
grouped_sum = df.groupby(['region', 'year'])['sales'].sum().reset_index()
print("\nGrouped by region and year (sum of sales):")
print(grouped_sum)

#   region  year  sales
# 0   East  2021    110
# 1   East  2022    130
# 2  North  2021    220
# 3  North  2022    200
# 4  South  2021    150
# 5  South  2022    170


# Group by region and year, multiple aggregations
grouped_agg = df.groupby(['region', 'year'])['sales'].agg(['sum', 'mean', 'count']).reset_index()
print("\nGrouped by region and year (sum, mean, count):")
print(grouped_agg)

#   region  year  sum   mean  count
# 0   East  2021  110  110.0      1
# 1   East  2022  130  130.0      1
# 2  North  2021  220  110.0      2
# 3  North  2022  200  200.0      1
# 4  South  2021  150  150.0      1
# 5  South  2022  170  170.0      1