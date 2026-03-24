import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.title("Dashboard Monitoring Storage")

conn = sqlite3.connect("database.db")

df = pd.read_sql(
    "SELECT * FROM data_storage",
    conn
)

# FILTER

item = st.selectbox(
    "ITEM",
    df["ITEM"].unique()
)

df_item = df[df["ITEM"] == item]


parameter = st.selectbox(
    "PARAMETER",
    df_item["PARAMETER"].unique()
)

df_param = df_item[df_item["PARAMETER"] == parameter]


fig = px.line(
    df_param,
    x="TANGGAL",
    y="NILAI"
)

st.plotly_chart(fig)

st.dataframe(df_param)
