import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned dataset
df = pd.read_csv("cleaned_food_delivery.csv")

# 2. Orders by city
plt.figure(figsize=(8, 5))
df["city"].value_counts().plot(kind="bar")
plt.title("Orders by City")
plt.xlabel("City")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("visualizations/orders_by_city.png")
plt.show()

# 3. Order status distribution
plt.figure(figsize=(7, 5))
df["order_status"].value_counts().plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("visualizations/popular_cuisine.png")
plt.show()

# 4. Customer rating distribution
plt.figure(figsize=(7, 5))
df["customer_rating"].dropna().plot(
    kind="hist", bins=5, edgecolor="black"
)
plt.title("Customer Rating Distribution")
plt.xlabel("Customer Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visualizations/delivery_time.png")
plt.show()

# 5. Delivery time distribution
plt.figure(figsize=(8, 5))
df["total_delivery_time_mins"].plot(
    kind="hist", bins=10, edgecolor="black"
)
plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("visualizations/order_status.png")
plt.show()

print("All visualizations created successfully!")