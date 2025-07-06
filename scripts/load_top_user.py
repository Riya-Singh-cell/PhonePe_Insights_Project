import os
import json
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')
base_path = '../pulse/data/top/user/country/india'

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
                    data = json_data.get("data", {}).get("states", [])

                    for state in data:
                        row = {
                            "year": int(year),
                            "quarter": int(quarter),
                            "state": state.get("name"),
                            "registered_users": state.get("registeredUsers"),
                            "app_opens": state.get("appOpens")
                        }
                        all_data.append(row)
                except Exception as e:
                    print(f"❌ Error in {file_path}: {e}")

df = pd.DataFrame(all_data)

try:
    df.to_sql('top_user', engine, if_exists='append', index=False)
    print("✅ Data loaded successfully into 'top_user' table!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
