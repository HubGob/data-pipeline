from sqlalchemy import create_engine
import pandas as pd

def save_to_db(df, table_name, db_path="data/processed/pipeline.db"):
    """Save dataframe to SQLite."""
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Saved to {db_path}, table: {table_name}")

def query_sql(sql, db_path="data/processed/pipeline.db"):
    """Run SQL query."""
    engine = create_engine(f"sqlite:///{db_path}")
    return pd.read_sql(sql, engine)