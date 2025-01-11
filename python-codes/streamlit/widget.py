import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")

if name: 
    st.write(f"Hello {name}, how are you today?")

age = st.slider("Enter your age", 0, 100, 32)

st.write(f"You are {age} years old")

options = ["Java", "Python", "Kotlin"]

choice = st.selectbox("Choose your favourite language ",options)

st.write(f"You selected {choice}")

upload_file = st.file_uploader("choose a csv file ", type = "csv")

try:
    if upload_file:
        df = pd.read_csv(upload_file)
        st.write(df)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"Unable to process file {e}")
