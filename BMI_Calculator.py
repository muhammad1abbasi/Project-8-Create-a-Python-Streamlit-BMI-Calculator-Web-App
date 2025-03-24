import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height/100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write(f"### BMI Categories ###")
st.wirte("- Underweight: BMI less then 18.5")
st.write("- Normal wight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 2 and 29.9 ")
st.write("- Obesity: BMI 30 or greater")