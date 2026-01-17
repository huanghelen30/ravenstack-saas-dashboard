import pandas as pd
import streamlit as st

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