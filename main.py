from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

CONFIG_PATH = "config/config.yaml"

def run_pipeline():
    videos_df, category_df = extract_data(CONFIG_PATH)
    cleaned_df = transform_data(videos_df, category_df, CONFIG_PATH)
    load_data(cleaned_df, CONFIG_PATH)

if __name__ == "__main__":
    run_pipeline()
    print("Pipeline completed successfully!")