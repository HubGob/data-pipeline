#!/usr/bin/env python3
"""Run complete data pipeline."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.pipeline.load import load_csv
from src.pipeline.clean import clean_data
from src.pipeline.database import save_to_db, query_sql

def main():
    print("=" * 50)
    print("STARTING PIPELINE")
    print("=" * 50)
    
    # Step 1: Extract
    print("\n[1/4] Extracting data...")
    df = load_csv("data/raw/sample.csv")
    
    # Step 2: Transform
    print("\n[2/4] Cleaning data...")
    df = clean_data(df)
    
    # Step 3: Load
    print("\n[3/4] Saving to database...")
    save_to_db(df, "clean_data")
    
    # Step 4: Verify
    print("\n[4/4] Verifying...")
    result = query_sql("SELECT COUNT(*) as count FROM clean_data")
    print(f"Total rows in database: {result['count'].iloc[0]}")
    
    print("\n" + "=" * 50)
    print("PIPELINE COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()