import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load data
df = pd.read_sql("SELECT * FROM map_transaction", engine)

# Show sample data
print("📊 Data Sample:")
print(df.head())

print("\n🧹 Null values:")
print(df.isnull().sum())

# 1. Total Transactions per State
state_txn = df.groupby("state")["count"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(14, 8))
sns.barplot(data=state_txn, x="count", y="state", palette="coolwarm")
plt.title("Total Transactions by State")
plt.xlabel("Total Transaction Count")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 2. Total Amount per State
state_amount = df.groupby("state")["amount"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(14, 8))
sns.barplot(data=state_amount, x="amount", y="state", palette="magma")
plt.title("Total Transaction Amount by State")
plt.xlabel("Total Amount (INR)")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 3. Top 5 states comparison: Count vs Amount
top5 = state_txn.head(5).merge(state_amount.head(5), on="state", suffixes=("_count", "_amount"))

fig, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top5, x="state", y="count", ax=ax1, color='skyblue', label='Transaction Count')
ax2 = ax1.twinx()
sns.lineplot(data=top5, x="state", y="amount", ax=ax2, marker='o', color='red', label='Transaction Amount')

ax1.set_ylabel("Count")
ax2.set_ylabel("Amount (INR)")
plt.title("Top 5 States: Count vs Amount")
plt.tight_layout()
plt.show()
