import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO # BytesIO used for buffer memory to store or capture images

   
# Helper function to load image from a URL
def load_image_from_url(url):
    # Add a User-Agent header to mimic a browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=10) # Added a 10-second timeout
        
    return Image.open(BytesIO(response.content))

# Elephant image URL
elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"

elephant= load_image_from_url(elephant_url)

# display an original image
plt.figure(figsize=(6,4))
plt.imshow(elephant)
plt.title('Elephant')
plt.axis('off')
plt.show()

# Convert image to Numpy array and print shape
elephant_np=np.array(elephant)
print("Elephant image shape:",elephant_np.shape)

# Display Grayscale Image
elephant_gray=elephant.convert("L")

plt.figure(figsize=(8,6))
plt.imshow(elephant_gray, cmap="gray")
plt.title('Elephant_GrayScale')
plt.axis('off')
plt.show()