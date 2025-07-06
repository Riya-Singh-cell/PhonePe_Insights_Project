# scripts/transform_and_export.py

import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Load each table
tables = [
    "aggregated_transaction",
    "aggregated_user",
    "map_transaction",
    "map_user",
    "top_transaction",
    "top_user"
]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)

    # Simple cleanup: lowercase columns
    df.columns = [col.lower() for col in df.columns]

    # Save to new transformed folder
    path = f"exports/transformed/{table}.csv"
    df.to_csv(path, index=False)
    print(f"✅ Transformed CSV saved: {path}")
