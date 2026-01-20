import pandas as pd
import streamlit as st
from data_processing.load_and_clean import load_accounts
from data_processing.metrics import active_accounts, churn_rate, churn_by_plan_tier, signup_growth

st.title("Ravenstack Dashboard")

# -----------------------
# Data Loading
# -----------------------

accounts_df_cleaned = load_accounts()

active_accounts_df = active_accounts(accounts_df_cleaned)
churn_plan_df = churn_by_plan_tier(accounts_df_cleaned)
signup_growth_monthly_df = signup_growth(accounts_df_cleaned, period="month")

st.subheader("Core Metrics")
st.metric("Total Accounts", len(accounts_df_cleaned))
st.metric("Active Accounts", len(active_accounts_df))
st.metric("Churn Rate", f"{churn_rate(accounts_df_cleaned):.1%}")

st.subheader("Churn Rate by Plan Tier")
st.dataframe(churn_plan_df)

st.subheader("Signup Growth (Monthly)")
st.line_chart(signup_growth_monthly_df.set_index("signup_month")["new_accounts"])
