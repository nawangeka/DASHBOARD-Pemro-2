import streamlit as st
import pandas as pd


def load_data():
    df= pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def show_data():
    df= load_data()
    st.subheader("🦠 Data Kasus Covid-19 di 🔴")
    st.dataframe(df.head(10))
    st.subheader("📊Statistika Deskriptif")
    st.write(df.describe())

def total_kasus():
    df= load_data()
    st.subheader("Total Kasus Covid-19")
    st.write(f"Total Kasus Covid-19 {df["Total Cases"].sum()}")
    
def kolom_tertentu():
    df= load_data()
    st.subheader("Kolom tertentu")
    st.write(df.iloc[:, 2: 9])
    
def nama():
    st.caption("Nawang Eka / 184240009")               

