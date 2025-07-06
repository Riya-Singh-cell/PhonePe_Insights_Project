import os
import json
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:password@localhost:5432/phone_pe')

# Path to the JSON folder
base_path = '../pulse/data/aggregated/user/country/india'

# Collect all data
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
                    aggregated = data.get("aggregated", {})
                    registered_users = aggregated.get("registeredUsers")
                    app_opens = aggregated.get("appOpens")

                    users_by_device = data.get("usersByDevice", [])

                    for device in users_by_device:
                        row = {
                            "year": int(year),
                            "quarter": int(quarter),
                            "brand": device.get("brand"),
                            "count": device.get("count"),
                            "percentage": device.get("percentage"),
                            "registered_users": registered_users,
                            "app_opens": app_opens
                        }
                        all_data.append(row)

                except Exception as e:
                    print(f"❌ Error in {file_path}: {e}")

# Convert to DataFrame
df = pd.DataFrame(all_data)

# Load into SQL
try:
    df.to_sql('aggregated_user', engine, if_exists='append', index=False)
    print("✅ Data loaded successfully into 'aggregated_user' table!")
except Exception as e:
    print(f"❌ Failed to load data: {e}")
