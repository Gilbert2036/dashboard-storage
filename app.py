import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data_bersih.csv")

st.title("Dashboard Monitoring Storage")

# =====================
# PILIH TANGGAL
# =====================

tanggal = st.selectbox(
    "Pilih Tanggal",
    sorted(df["TANGGAL"].unique())
)

df_tanggal = df[df["TANGGAL"] == tanggal]


# =====================
# PILIH PARAMETER
# =====================

parameter = st.selectbox(
    "Pilih Parameter",
    sorted(df_tanggal["PARAMETER"].unique())
)

df_param = df_tanggal[df_tanggal["PARAMETER"] == parameter]


# =====================
# TABEL
# =====================

st.subheader(f"Data tanggal {tanggal}")
st.dataframe(df_param, use_container_width=True)


# =====================
# GRAFIK SEMUA ITEM
# =====================

fig = px.bar(
    df_param,
    x="ITEM",
    y="NILAI",
    color="ITEM",
    title=f"{parameter} tanggal {tanggal}"
)

st.plotly_chart(fig, use_container_width=True)


# =====================
# KETERANGAN / REDAKSI
# =====================

st.markdown("### Keterangan")

st.write(
    f"""
    Pada tanggal {tanggal}, nilai parameter **{parameter}**
    ditampilkan untuk seluruh storage, bunker, cangkang,
    dan jangkos yang tersedia pada sistem monitoring.

    Data ini digunakan sebagai bahan evaluasi operasional harian.
    """
)
