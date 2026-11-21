import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_food_delivery.csv")

# 1. Most popular city
print("\nOrders by City:")
print(df["city"].value_counts())

# 2. Most popular cuisine
print("\nPopular Cuisine:")
print(df["cuisine_type"].value_counts())

# 3. Average delivery time
print("\nAverage Delivery Time:")
print(df["total_delivery_time_mins"].mean())

# 4. Order status analysis
print("\nOrder Status:")
print(df["order_status"].value_counts())

# 5. Customer ratings
print("\nAverage Rating:")
print(df["customer_rating"].mean())