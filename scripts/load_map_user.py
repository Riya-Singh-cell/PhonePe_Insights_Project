import os
import json
import pandas as pd
from sqlalchemy import create_engine

# Set up PostgreSQL connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Adjust the path as per your folder structure
base_path = '../pulse/data/map/user/hover/country/india'

all_data = []

# Loop through years
for year in os.listdir(base_path):
    year_path = os.path.join(base_path, year)
    if not os.path.isdir(year_path):
        continue

    # Loop through quarters
    for file in os.listdir(year_path):
        if file.endswith('.json'):
            quarter = file.replace('.json', '')
            file_path = os.path.join(year_path, file)

            with open(file_path, 'r') as f:
                try:
                    json_data = json.load(f)
                    hover_data = json_data.get("data", {}).get("hoverData", {})

                    for state, metrics in hover_data.items():
                        row = {
                            "year": int(year),
                            "quarter": int(quarter),
                            "state": state,
                            "registered_users": metrics.get("registeredUsers", 0),
                            "app_opens": metrics.get("appOpens", 0)
                        }
                        all_data.append(row)

                except Exception as e:
                    print(f"❌ Error in {file_path}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Load into PostgreSQL
try:
    df.to_sql('map_user', engine, if_exists='append', index=False)
    print("✅ Data loaded successfully into 'map_user' table!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
