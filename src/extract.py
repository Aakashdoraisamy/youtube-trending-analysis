import pandas as pd
import json
import yaml

def extract_data(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    csv_path = config["data_paths"]["raw_csv"]
    json_path = config["data_paths"]["raw_json"]

    print("📥 Extracting data from raw files...")
    videos_df = pd.read_csv(csv_path)
    with open(json_path, "r") as f:
        json_data = json.load(f)
    category_df = pd.json_normalize(json_data["items"])

    return videos_df, category_df
