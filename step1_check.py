import pandas as pd
df = pd.read_csv("food_delivery_data_100_records.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())