def active_accounts(df):
    return df[df["churn_flag"] == False]

def churned_accounts(df):
    return df[df["churn_flag"] == True]

def churn_rate(df):
    if len(df) == 0:
        return 0.0
    return df["churn_flag"].mean()

def churn_by_plan_tier(df):
    return (
        df.groupby("plan_tier")["churn_flag"]
        .mean()
        .reset_index(name="churn_rate") 
    )

def signup_growth(df, period="month"):
    if df.empty:
        return pd.DataFrame(columns=["signup_month", "new_accounts"])

    if period == "month":
        out = (
            df.groupby("signup_month")["account_id"]
            .count()
            .reset_index(name="new_accounts")
        )
    elif period == "quarter":
        out = (
            df.groupby("signup_quarter")["account_id"]
            .count()
            .reset_index(name="new_accounts")
        )
    else:
        raise ValueError("Unsupported period")

    return out
