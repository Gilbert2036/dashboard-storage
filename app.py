import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data_bersih.csv")

st.title("Dashboard Monitoring Storage")

# =====================
# FILTER ITEM
# =====================

item = st.selectbox(
    "Pilih ITEM",
    sorted(df["ITEM"].unique())
)

df_item = df[df["ITEM"] == item]

# =====================
# FILTER PARAMETER
# =====================

parameter = st.selectbox(
    "Pilih PARAMETER",
    sorted(df_item["PARAMETER"].unique())
)

df_param = df_item[df_item["PARAMETER"] == parameter]

# =====================
# FILTER TANGGAL
# =====================

tanggal = st.multiselect(
    "Pilih Tanggal",
    sorted(df_param["TANGGAL"].unique()),
    default=sorted(df_param["TANGGAL"].unique())
)

df_final = df_param[df_param["TANGGAL"].isin(tanggal)]

# =====================
# TABEL
# =====================

st.subheader("Data")
st.dataframe(df_final, use_container_width=True)

# =====================
# GRAFIK
# =====================

fig = px.line(
    df_final,
    x="TANGGAL",
    y="NILAI",
    markers=True,
    title=f"{item} - {parameter}"
)

st.plotly_chart(fig, use_container_width=True)
