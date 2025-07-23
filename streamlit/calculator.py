import streamlit as st 

st.title('Simple Calculator App')

st.header('Enter Numbers:')
num1=st.number_input('Enter First Number:', step=1)
num2=st.number_input('Enter Second Number:',step=1)

operation=st.selectbox("Select Operation:",["Addition", "Substraction", "Multiplication", "Division"])

if st.button("Calculate"):
    st.subheader("Result:")
    
    if operation == "Addition":
        result = num1 + num2
        st.success(f'{num1} + {num2} = {result}')
    elif operation == "Substraction":
        result = num1 - num2
        st.success(f'{num1} - {num2} = {result}')
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f'{num1} * {num2} = {result}')
    elif operation == "Division":
        if(num2==0):
            st.error("Can not divide by Zero")
        else:
            result = num1 / num2
            st.success(f'{num1} / {num2} = {result}')




