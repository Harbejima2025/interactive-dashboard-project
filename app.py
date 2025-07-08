# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Dashboard Example")

# Load data
df = pd.read_csv("data/sample_data.csv")

# Sidebar filter
selected_option = st.sidebar.selectbox("Select Category", df["category"].unique())

# Filtered data
filtered_df = df[df["category"] == selected_option]

# Show chart
fig = px.bar(filtered_df, x="subcategory", y="value", color="subcategory")
st.plotly_chart(fig)

# Show table
st.dataframe(filtered_df)
