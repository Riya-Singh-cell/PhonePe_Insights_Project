import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load data
df = pd.read_sql("SELECT * FROM map_user", engine)

# Show sample data
print("📊 Data Sample:")
print(df.head())

# Check for nulls
print("\n🧹 Null values:")
print(df.isnull().sum())

# 1. Total Registered Users by State
state_users = df.groupby("state")["registeredUsers"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(14, 8))
sns.barplot(data=state_users, x="registeredUsers", y="state", palette="crest")
plt.title("Total Registered Users by State")
plt.xlabel("Registered Users")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 2. Total App Opens by State (if meaningful)
state_app_opens = df.groupby("state")["appOpens"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(14, 8))
sns.barplot(data=state_app_opens, x="appOpens", y="state", palette="rocket")
plt.title("Total App Opens by State")
plt.xlabel("App Opens")
plt.ylabel("State")
plt.tight_layout()
plt.show()

# 3. Top 5 States: Registered Users vs App Opens
top5 = state_users.head(5).merge(state_app_opens.head(5), on="state", suffixes=("_users", "_opens"))

fig, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top5, x="state", y="registeredUsers", ax=ax1, color='orange', label='Registered Users')
ax2 = ax1.twinx()
sns.lineplot(data=top5, x="state", y="appOpens", ax=ax2, marker='o', color='black', label='App Opens')

ax1.set_ylabel("Registered Users")
ax2.set_ylabel("App Opens")
plt.title("Top 5 States: Registered Users vs App Opens")
plt.tight_layout()
plt.show()

