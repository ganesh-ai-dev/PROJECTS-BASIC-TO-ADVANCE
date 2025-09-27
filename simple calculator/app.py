# app.py
import streamlit as st
import calculator 

st.title("Simple Calculator")

num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)

operation = st.selectbox("Choose operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = calculator.add(num1, num2)
    elif operation == "Subtraction":
        result = calculator.subtract(num1, num2)
    elif operation == "Multiplication":
        result = calculator.multiplication(num1, num2)
    elif operation == "Division":
        result = calculator.division(num1, num2)
    
    st.success(f"Result: {result}")
