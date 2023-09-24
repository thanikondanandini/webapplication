import streamlit as st
st.write("# Hello World")
num1 = st.number_input("Pick a number 1")
num2 = st.number_input("Pick a number 2")


if st.button("Click me"):
    st.write(num1 + num2)
    st.balloons()
    st.success('Success message')