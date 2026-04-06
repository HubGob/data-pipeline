import pandas as pd

def clean_data(df):
    """Clean the dataframe."""
    # Drop rows with missing values
    df = df.dropna()
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    print(f"Cleaned: {len(df)} rows remaining")
    return df