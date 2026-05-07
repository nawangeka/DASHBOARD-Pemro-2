import streamlit as st
import pandas as pd
from data import show_data, kolom, select_year, load_data, filter_data, pie_chart1, bar_chart1, bar_chart2, map_chart, select_location



#judul dashboard
def judul ():
    st.title("📊 Dashboard  Covid-19")
    st.write("Selamat datang di dashboard Covid-19 disini anda dapat melihat data pribadi anda")


st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman data"])


if menu == "Home":
    judul()
    df = load_data()
    year = select_year()
    location = select_location(df)
    df_filtered = filter_data(df, year=year, location=location)
    kolom(df_filtered)
    pie_chart1(df_filtered, key="pie_home")
    bar_chart1(df_filtered)
    bar_chart2(df_filtered)
    map_chart(df_filtered, year=year)

    
elif menu == "Halaman data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year=year)
    show_data(df_filtered)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "© 2026 Nawang Eka - 184240009"
)
# Selesai: Dashboard Covid-19 berhasil diimplementasikan dengan navigasi interaktif.