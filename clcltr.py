import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Create two input fields for numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Create a dropdown to select the operation
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Define a function to perform the selected operation
def calculate(n1, n2, op):
    if op == "Add":
        return n1 + n2
    elif op == "Subtract":
        return n1 - n2
    elif op == "Multiply":
        return n1 * n2
    elif op == "Divide":
        return n1 / n2 if n2 != 0 else "Error: Division by zero"

# Calculate the result based on user input
result = calculate(num1, num2, operation)

# Display the result
st.write(f"Result: {result}")
