import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for the two numbers
    num1 = st.number_input("Enter first number", value=0.0, format="%f")
    num2 = st.number_input("Enter second number", value=0.0, format="%f")

    # Radio buttons to select the operation
    operation = st.radio("Select an operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform the calculation based on the selected operation
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            return

    # Display the result
    st.write("Result:", result)

if __name__ == "__main__":
    main()

  