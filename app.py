import pandas as pd
import streamlit as st
from data_processing.load_and_clean import load_accounts
from data_processing.metrics import active_accounts, churn_rate

st.title("Ravenstack Dashboard")
st.write("Environment Check: Streamlit is running successfully!")

# -----------------------
# Data Loading
# -----------------------

accounts_df = pd.read_csv("data/raw/ravenstack_accounts.csv")
st.write("Accounts Data Loaded:")
st.dataframe(accounts_df.head())

st.write("Accounts Columns:")
st.write(accounts_df.columns.tolist())

accounts_df_cleaned = load_accounts()

st.subheader("Cleaned Accounts Data")
st.dataframe(accounts_df_cleaned.head())

st.subheader("Schema Check")
st.write(accounts_df_cleaned.dtypes)

active_accounts_df = active_accounts(accounts_df_cleaned)

st.subheader("Core Metrics")
st.metric("Total Accounts", len(accounts_df_cleaned))
st.metric("Active Accounts", len(active_accounts_df))
st.metric("Churn Rate", f"{churn_rate(accounts_df_cleaned):.1%}")

st.subheader("Churn Rate by Plan Tier")

churn_by_plan = (
    accounts_df_cleaned
    .groupby("plan_tier")["churn_flag"]
    .mean()
    .reset_index(name="churn_rate")
)

st.dataframe(churn_by_plan)