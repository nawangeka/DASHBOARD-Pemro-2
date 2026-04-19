import streamlit as st
from data import*


def judul():
    st.title("📊Dashboard Covid-19")
    st.write("Selamat datang di dashboard Covid-19! Disini Anda dapat melihat data pribadi")


st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman data",])
if menu == "Home":
    judul()
    nama()
elif menu == "Halaman data":
    judul()
    show_data()
    nama()    

# Selesai: Dashboard Covid-19 berhasil diimplementasikan dengan navigasi interaktif.    