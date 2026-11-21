import pandas as pd

df = pd.read_csv("food_delivery_data_100_records.csv")

# 1. Duplicate rows check & remove
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()

# 2. Convert order_datetime to proper datetime & extract hour/day
df["order_datetime"] = pd.to_datetime(df["order_datetime"], errors="coerce")
df["order_hour"] = df["order_datetime"].dt.hour
df["order_day"] = df["order_datetime"].dt.day_name()

# 3. Check missing values per column
print("\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 4. Save cleaned file
df.to_csv("cleaned_food_delivery.csv", index=False)
print("\nSaved cleaned_food_delivery.csv! New shape:", df.shape)