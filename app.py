# store this as app.py
import streamlit as st

st.title("Addition App")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if st.button("Add"):
    result = num1 + num2
    st.write(f"The result is {result}")