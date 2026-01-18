def active_accounts(df):
    return df[df["churn_flag"] == False]

def churned_accounts(df):
    return df[df["churn_flag"] == True]

def churn_rate(df):
    if len(df) == 0:
        return 0.0
    return df["churn_flag"].mean()