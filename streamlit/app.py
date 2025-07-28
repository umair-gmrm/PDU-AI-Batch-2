import streamlit as st


st.title("Hello, Streamlit!")



name = st.text_input("Enter your name:", key="name_input")

if name:
    st.write(f"Hello, {name}!")