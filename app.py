# app.py

import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Live Sales Dashboard from Google Sheets")

# Authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Load Sheet
sheet = client.open("Sales_Data").sheet1  # Use your sheet name here
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Interactive Chart
st.sidebar.header("🔎 Filter")
categories = df["Category"].unique().tolist()
selected = st.sidebar.multiselect("Select Category", categories, default=categories)

filtered_df = df[df["Category"].isin(selected)]
st.dataframe(filtered_df)

fig = px.bar(filtered_df, x="Date", y="Sales", color="Category", title="Sales by Category")
st.plotly_chart(fig, use_container_width=True)
