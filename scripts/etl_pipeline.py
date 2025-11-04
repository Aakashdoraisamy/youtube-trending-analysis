import pandas as pd
import sqlite3

df = pd.read_csv('../raw_data/cleaned_INvideos.csv')

conn = sqlite3.connect('../database/youtube.db')

df.to_sql('youtube_trending', conn, if_exists='replace', index=False)

print("✅ Data successfully loaded into SQLite database.")

conn.close()
