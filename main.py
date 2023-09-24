import streamlit as st
st.write("# Hello World")
num1 = st.number_input("Pick a number 1")
num2 = st.number_input("Pick a number 2")


if st.button("Click me"):
    st.write(num1 + num2)
    st.balloons()
    st.snow()
    st.toast('Warming up...')
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')