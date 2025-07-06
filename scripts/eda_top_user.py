import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
os.makedirs("exports", exist_ok=True)
# DB Connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load data
df = pd.read_sql("SELECT * FROM top_user", engine)

# Data check
print("📊 Sample:")
print(df.head())

print("\n🧹 Nulls:")
print(df.isnull().sum())

# Export raw data
df.to_csv("exports/top_user_raw.csv", index=False)
print("📁 CSV saved: exports/top_user_raw.csv")

# 1. Top districts by registered users
top_users = df.groupby("state")["registered_users"].sum().sort_values(ascending=False).reset_index().head(10)


plt.figure(figsize=(12, 6))
sns.barplot(data=top_users, x="registered_users", y="state", palette="cubehelix")
plt.title("Top 10 Districts by Registered Users")
plt.xlabel("Registered Users")
plt.ylabel("District")
plt.tight_layout()
plt.show()

# 2. State-wise total users
state_users = df.groupby("state")["registered_users"].sum().sort_values(ascending=False).reset_index()


plt.figure(figsize=(14, 8))
sns.barplot(data=state_users, x="registered_users", y="state", hue=None, palette="icefire", legend=False)
plt.title("Total Registered Users by State (Top User Table)")
plt.xlabel("Registered Users")
plt.ylabel("State")
plt.tight_layout()
plt.show()
