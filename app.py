import pandas as pd
import streamlit as st
from data_processing.load_and_clean import load_accounts

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
