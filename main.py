import streamlit as st

st.title("Hi!")
st.write("I am Yamaan Faraz. Let me give you a little documentation")
st.write("First, then type this in terminal:")
st.code("pip install yf-calculator")
st.write("Then, in your  file, write this:")
st.code("from yf_calculator import yf_calculator-ui")
st.write("Then, write:")
st.code("yf_calculator_ui(csv_path='your .csv path with button goes here.',"
        "text='your text in the About Us button', title='Your page title goes here.', skip_first_column='Write True if want to skip, else, False.')")