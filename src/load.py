import sqlite3
import yaml
import os

def load_data(df, config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    db_path = config["database"]["name"]
    table_name = config["database"]["table_name"]

    print("💾 Loading data into SQLite...")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print(f"✅ Data loaded successfully into {table_name} table!")
