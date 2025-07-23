import streamlit as st 
import pandas as pd
import numpy as np

#--- Add title and Description ----
st.title('My First Streamlit App')
st.write('This is simple app to demonstrate the basic functionalities of streamlit')

# ----- Interactive Widgets in the Sidebar -----
st.sidebar.header('User Input Features')

# Text Input
user_name=st.sidebar.text_input('What is your name?',"OKULA YENUGU")

#Slider
age=st.sidebar.slider("Select Your Age", 0, 100, 35)

# Selectbox
favorite_color=st.sidebar.selectbox("What is your favorite color?",["Blue", "Red", "Green", "Yellow"])

# ------ Main Page Content -----
st.header(f'Welcome, {user_name}!')
st.write(f'You are {age} years old and your favorite color is: {favorite_color} ')

# ----- Displaying data-----
st.subheader('Here is some random data:')

# Create a sample DatFrame
data=pd.DataFrame(np.random.randn(5,5), columns=('col %d' % i for i in range(5)))

st.dataframe(data)

# --- Checkbox to show/hide content ---
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# --- Button to trigger an action ---
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")
