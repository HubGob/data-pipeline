from src.pipeline.load import load_csv
import pandas as pd
import os

def test_load_csv():
    """Test that load_csv returns a DataFrame."""
    # Create a test CSV
    test_data = "col1,col2\n1,2\n3,4"
    with open("data/raw/test.csv", "w") as f:
        f.write(test_data)
    
    # Test the function
    df = load_csv("data/raw/test.csv")
    
    # Check it's a DataFrame with 2 rows
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["col1", "col2"]

def test_load_csv_file_not_found():
    """Test that load_csv raises error for missing file."""
    try:
        load_csv("data/raw/nonexistent.csv")
        assert False, "Should have raised FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected