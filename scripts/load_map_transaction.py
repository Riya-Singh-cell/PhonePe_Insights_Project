import os
import json
import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Update this with your actual path
base_path = '../pulse/data/map/transaction/hover/country/india'

# For collecting all rows
all_data = []

# Walk through each year folder
for year in os.listdir(base_path):
    year_path = os.path.join(base_path, year)
    if not os.path.isdir(year_path):
        continue

    for file in os.listdir(year_path):
        if file.endswith('.json'):
            quarter = file.replace('.json', '')
            file_path = os.path.join(year_path, file)

            with open(file_path, 'r') as f:
                try:
                    json_data = json.load(f)

                    if "data" in json_data and "hoverDataList" in json_data["data"]:
                        for state_data in json_data["data"]["hoverDataList"]:
                            state = state_data.get("name")
                            metrics = state_data.get("metric", [])

                            for metric in metrics:
                                if metric["type"] == "TOTAL":
                                    row = {
                                        "year": int(year),
                                        "quarter": int(quarter),
                                        "state": state,
                                        "count": int(metric.get("count", 0)),
                                        "amount": float(metric.get("amount", 0))
                                    }
                                    all_data.append(row)
                    else:
                        print(f"⚠️ Skipping file (unexpected structure): {file_path}")

                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Insert into database
try:
    df.to_sql('map_transaction', engine, if_exists='append', index=False)
    print("✅ Data loaded successfully into 'map_transaction' table!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
