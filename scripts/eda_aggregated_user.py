import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load data
df = pd.read_sql("SELECT * FROM aggregated_user", engine)

# Basic Info
print("📊 Data Sample:")
print(df.head())

print("\n🧹 Null values:")
print(df.isnull().sum())

# 1. Top Mobile Brands by Count
plt.figure(figsize=(10, 6))
brand_counts = df.groupby("brand")["count"].sum().reset_index().sort_values("count", ascending=False)
sns.barplot(data=brand_counts, x="count", y="brand", palette="rocket")
plt.title("Top Mobile Brands by User Count")
plt.xlabel("User Count")
plt.ylabel("Brand")
plt.tight_layout()
plt.show()

# 2. Year-wise Usage of Top Brand
top_brand = brand_counts.iloc[0]["brand"]
brand_yearwise = df[df["brand"] == top_brand].groupby("year")["count"].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.lineplot(data=brand_yearwise, x="year", y="count", marker="o", color='green')
plt.title(f"Year-wise Usage of {top_brand}")
plt.xlabel("Year")
plt.ylabel("User Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Brand Percentage Distribution (Pie Chart)
brand_pie = df.groupby("brand")["count"].sum()
plt.figure(figsize=(8, 8))
plt.pie(brand_pie, labels=brand_pie.index, autopct='%1.1f%%', startangle=140)
plt.title("Mobile Brand Distribution")
plt.axis('equal')
plt.tight_layout()
plt.show()
