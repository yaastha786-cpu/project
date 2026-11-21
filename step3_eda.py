import pandas as pd

# 1. Load cleaned dataset
df = pd.read_csv("cleaned_food_delivery.csv")

# 2. Basic information
print("Dataset Shape:", df.shape)

print("\nDataset Information:")
print(df.info())

# 3. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 4. Average order value
print("\nAverage Order Value:")
print(df["order_value_inr"].mean())
# 5. Total revenue
print("\nTotal Revenue:")
print(df["order_value_inr"].sum())

# 6. Total orders
print("\nTotal Orders:")
print(df["order_id"].nunique())

# 7. Average customer rating
print("\nAverage Customer Rating:")
print(df["customer_rating"].mean())