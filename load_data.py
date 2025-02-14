import pandas as pd

# Load dataset
df = pd.read_csv("data/tracks.csv")

# Show first 5 rows
print(df.head())

# Check column names
print(df.columns)
