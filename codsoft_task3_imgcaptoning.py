#codsoft - Task 3 : = Image captioning 
# AI Internship

import streamlit as st
import requests
from PIL import Image
import io
import os 
import base64
API_URLL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"  
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
API_TOKEN = "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"
def caption_image(image):
         headers = {"Authorization": f"Bearer {API_TOKEN}"}
         img_byte_arr = io.BytesIO()
         image.save(img_byte_arr, format="JPEG")
         img_byte_arr.seek(0)
         response = requests.post(API_URLL, headers=headers, data=img_byte_arr.getvalue())
         return response.json()
     
st.subheader(":blue[Image processing Tools]")
st.write("----")
     
     # User selection for task'
tabs = st.tabs( ["Image Captioning"])
     
with tabs[0]:
         st.subheader(":orange[Image Captioning]")
         def query(image):
             headers = {"Authorization": f"Bearer {API_TOKEN}"}  # Use token if stored
             img_byte_arr = io.BytesIO()
             image.save(img_byte_arr, format="JPEG")
             img_byte_arr.seek(0)
             response = requests.post(API_URL, headers=headers, data=img_byte_arr.getvalue())
             return response.json()
     
     # Display file uploader and inference results
         uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
     
         if uploaded_file is not None:
             # Display the uploaded image
             image = Image.open(uploaded_file)
             
             st.image(image, caption="Uploaded Image", use_column_width=True)
     
             # Perform inference if user clicks the button
             if st.button("Run Inference"):
                 # Send image to model for inference
                 response = query(image)
     
                 # Display inference output
                 st.write("Inference Output:")
                 st.json(response)