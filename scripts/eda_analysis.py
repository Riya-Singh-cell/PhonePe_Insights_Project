import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Database connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load data from table
df = pd.read_sql("SELECT * FROM aggregated_transaction", engine)

# Check data
print("📊 Data Sample:")
print(df.head())

print("\n🧹 Null values:")
print(df.isnull().sum())

# Plot total transaction count by year
plt.figure(figsize=(10, 6))
sns.barplot(data=df.groupby("year")["count"].sum().reset_index(),
            x="year", y="count", palette="viridis")
plt.title("Total Transactions by Year")
plt.xlabel("Year")
plt.ylabel("Transaction Count")
plt.tight_layout()
plt.show()
sns.barplot(data=df.groupby("year")["amount"].sum().reset_index(),
            x="year", y="amount", palette="magma")
plt.title("Total Transaction Amount by Year")
plt.show()
sns.barplot(data=df.groupby("name")["count"].sum().reset_index().sort_values("count", ascending=False),
            x="count", y="name", palette="coolwarm")
plt.title("Total Transactions by Payment Type")
plt.show()
quarterly = df.groupby(["year", "quarter"])["count"].sum().reset_index()
quarterly["year_quarter"] = quarterly["year"].astype(str) + " Q" + quarterly["quarter"].astype(str)

sns.lineplot(data=quarterly, x="year_quarter", y="count", marker="o")
plt.xticks(rotation=45)
plt.title("Quarterly Transaction Count Over Time")
plt.tight_layout()
plt.show()
top_types = df.groupby("name")["amount"].sum().sort_values(ascending=False).head(5).reset_index()
sns.barplot(data=top_types, x="amount", y="name", palette="Blues_d")
plt.title("Top 5 Payment Types by Amount")
plt.show()


