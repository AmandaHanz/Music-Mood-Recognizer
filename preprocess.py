import pandas as pd

# Load dataset
df = pd.read_csv("data/tracks.csv")

# Select relevant features
features = ['danceability', 'energy', 'valence', 'tempo', 'speechiness', 'acousticness']
target = 'track_genre'

# Drop unnecessary columns
df = df[features + [target]]

# Drop missing values
df = df.dropna()

# Encode target labels as numbers
df[target] = df[target].astype('category').cat.codes

# Save processed dataset
df.to_csv("processed_tracks.csv", index=False)

print("Data Preprocessing Complete. Saved as 'processed_tracks.csv'.")
