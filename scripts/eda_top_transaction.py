import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
os.makedirs("exports", exist_ok=True)

# DB Connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load data
df = pd.read_sql("SELECT * FROM top_transaction", engine)

# Data check
print("📊 Sample:")
print(df.head())

print("\n🧹 Nulls:")
print(df.isnull().sum())

# Export raw data
df.to_csv("exports/top_transaction_raw.csv", index=False)
print("📁 CSV saved: exports/top_transaction_raw.csv")

# 1. Top districts by transaction amount
top_districts = df.groupby("entity_name")["amount"].sum().sort_values(ascending=False).reset_index().head(10)


plt.figure(figsize=(12, 6))
sns.barplot(data=top_districts, x="amount", y="entity_name", palette="plasma")
plt.title("Top 10 Districts by Transaction Amount")
plt.xlabel("Amount (INR)")
plt.ylabel("District")
plt.tight_layout()
plt.show()

# 2. Top districts by transaction count
top_counts = df.groupby("entity_name")["count"].sum().sort_values(ascending=False).reset_index().head(10)


plt.figure(figsize=(12, 6))
sns.barplot(data=top_counts, x="count", y="entity_name", hue=None, palette="flare", legend=False)
plt.title("Top 10 Districts by Transaction Count")
plt.xlabel("Transaction Count")
plt.ylabel("District")
plt.tight_layout()
plt.show()
