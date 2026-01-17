import pandas as pd

def load_accounts():
    df = pd.read_csv("data/raw/ravenstack_accounts.csv")
    
    # Standardize columns
    df.columns = df.columns.str.lower().str.strip()
    
    # Drop rows without account_id
    df = df.dropna(subset=["account_id"])
    
    df["account_id"] = df["account_id"].astype(str)
    
    return df