import pandas as pd

def load_accounts():
    df = pd.read_csv("data/raw/ravenstack_accounts.csv")
    
    # Standardize columns
    df.columns = df.columns.str.lower().str.strip()
    
    # Drop rows without account_id
    df = df.dropna(subset=["account_id"])
    
    # Convert account_id to string
    df["account_id"] = df["account_id"].astype(str)
    
    # Convert signup_date to datetime
    df["signup_date"] = pd.to_datetime(
    df["signup_date"],
    errors="coerce"
    )
    
    # Drop rows without signup_date
    df = df.dropna(subset=["signup_date"])
    
    assert df["account_id"].isna().sum() == 0, "Missing account_id"
    assert df["signup_date"].isna().sum() == 0, "Missing signup_date"
    assert (df["seats"] >= 0).all(), "Negative seat counts found"

    return df