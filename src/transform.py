import pandas as pd
import os
import yaml

def transform_data(videos_df, category_df, config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    cleaned_csv = config["data_paths"]["cleaned_csv"]

    print("🔧 Cleaning and transforming data...")

    category_df = category_df[["id", "snippet.title"]]
    category_df.columns = ["category_id", "category_name"]
    videos_df["category_id"] = videos_df["category_id"].astype(str)

    merged_df = pd.merge(videos_df, category_df, on="category_id", how="left")
    merged_df = merged_df.dropna(subset=["title", "views"])
    merged_df = merged_df.drop_duplicates(subset=["video_id"])

    cleaned_df = merged_df[[
        "video_id", "title", "channel_title", "category_name",
        "views", "likes", "comment_count"
    ]]

    os.makedirs(os.path.dirname(cleaned_csv), exist_ok=True)
    cleaned_df.to_csv(cleaned_csv, index=False)
    print(f"✅ Cleaned data saved at {cleaned_csv}")

    return cleaned_df
