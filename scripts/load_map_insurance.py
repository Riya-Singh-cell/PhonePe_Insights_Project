import os
import json
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Path to the JSON files
base_path = '../pulse/data/map/insurance/hover/country/india'

# Collect data
all_data = []

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
                    data = json_data.get("data", {}).get("hoverDataList", [])

                    for state_data in data:
                        state = state_data.get("name")
                        metrics_list = state_data.get("metric", [])

                        for metric in metrics_list:
                            row = {
                                "year": int(year),
                                "quarter": int(quarter),
                                "state": state,
                                "count": metric.get("count"),
                                "amount": metric.get("amount")
                            }
                            all_data.append(row)

                except Exception as e:
                    print(f"❌ Error in {file_path}: {e}")

# Upload to DataFrame and SQL
df = pd.DataFrame(all_data)

try:
    df.to_sql('map_insurance', engine, if_exists='append', index=False)
    print("✅ Data loaded successfully into 'map_insurance' table!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
