import pandas as pd

def load_csv(filepath):
    """Load CSV file."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows")
    print(df.head())
    return df

if __name__ == "__main__":
    load_csv("data/raw/sample.csv")