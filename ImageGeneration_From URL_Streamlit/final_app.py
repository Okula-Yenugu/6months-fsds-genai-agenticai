import streamlit as st 
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set streamlit page config
st.set_page_config(page_title="Elephant Image Processor", layout="centered")

# Title
st.title("Elephant Image - Multi Color Channel Visualizer")

# load Image from URL
@st.cache_data
def load_image():
    url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return Image.open(BytesIO(response.content)).convert("RGB")

# Load and display image
elephant = load_image()
st.image(elephant, caption="Original Elephant Image", use_column_width=True)

# Covert Image to NumPy array
elephant_np= np.array(elephant)
R, G, B= elephant_np[:, :, 0], elephant_np[:, :, 1], elephant_np[:, :,2]

# Create Channel Images
red_img=np.zeros_like(elephant_np)
green_img=np.zeros_like(elephant_np)
blue_img=np.zeros_like(elephant_np)

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

elephant_gray= elephant.convert("L")
elephant_gray_np=np.array(elephant_gray)

# Plot using matplotlib with color map
fig, ax=plt.subplots(figsize=(4,2))
im=ax.imshow(elephant_gray_np,colormap)
plt.axis("off")

st.pyplot(fig)
