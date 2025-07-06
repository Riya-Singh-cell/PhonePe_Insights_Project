import os
import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')
base_path = '../pulse/data/top/insurance/country/india'

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
                    data = json_data.get("data", {})
                    state = data.get("name")
                    for entry in data.get("districts", []) + data.get("pincodes", []):
                        row = {
                            "year": int(year),
                            "quarter": int(quarter),
                            "state": state,
                            "entity_name": entry.get("entityName"),
                            "entity_type": entry.get("entityType"),
                            "count": entry.get("metric", {}).get("count"),
                            "amount": entry.get("metric", {}).get("amount")
                        }
                        all_data.append(row)
                except Exception as e:
                    print(f"❌ Error in {file_path}: {e}")

df = pd.DataFrame(all_data)

try:
    df.to_sql('top_insurance', engine, if_exists='append', index=False)
    print("✅ Data loaded into 'top_insurance' table!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
