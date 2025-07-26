import streamlit as st 
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

#set streamlit page config
st.set_page_config(page_title="My Image Processor", layout="centered")

#title
st.title("My Image - Multi Color Channel Visualizer")

# Load image from local path
@st.cache_data
def load_image():
    path=r"d:\brand-factory\public\images\kids.jpg"
    return Image.open(path).convert("RGB")

# Load and Display Image
myImage=load_image()
st.image(myImage, caption="Original My Image", use_column_width=True)

# Covert Image to NumPy array
myImage_np= np.array(myImage)
R, G, B= myImage_np[:, :, 0], myImage_np[:, :, 1], myImage_np[:, :,2]

# Create Channel Images
red_img=np.zeros_like(myImage_np)
green_img=np.zeros_like(myImage_np)
blue_img=np.zeros_like(myImage_np)

red_img[:, :, 0]=R
green_img[:, :, 1]=G
blue_img[:, :, 2]=B

# Display RGB Channels
st.subheader("RGB Channel Visualization")
col1, col2, col3=st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_column_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_column_width=True)
    
with col3:
    st.image(blue_img, caption="Blue Channel", use_column_width=True)
    
# Grayscale + Color map
st.subheader("Colormapped GrayScale Image")

colormap = st.selectbox(
    "Chooses a matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

myImage_gray= myImage.convert("L")
myImage_gray_np=np.array(myImage_gray)

# Plot using matplotlib with color map
fig, ax=plt.subplots(figsize=(4,2))
im=ax.imshow(myImage_gray_np,colormap)
plt.axis("off")

st.pyplot(fig)
