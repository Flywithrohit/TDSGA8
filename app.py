import streamlit as st

def FindLargest(number1, number2, number3):
    if (number1 >= number2 and number1 >= number3):
        return number1
    elif (number2 >= number1 and number2 >= number3):
        return number2
    else:
        return number3

def main():
    st.title("TDS GA Week 8 : This app will compare the largest number among the provided numbers as inputs")
    st.write("Enter the numbers to proceed")

    number1 = st.number_input("Enter First Number:", step=1.0)
    number2 = st.number_input("Enter Second Number:", step=1.0)
    number3 = st.number_input("Enter Third Number:", step=1.0)

    if st.button("Get Largest Number"):
        largest = FindLargest(number1, number2, number3)
        st.success(f"The largest number among the provided inputs is: {largest}")

if __name__ == "__main__":
    main()
