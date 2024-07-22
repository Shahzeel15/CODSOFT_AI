
import cv2
import streamlit as st
import numpy as np
from PIL import Image

def detect_faces(image):
    # Convert the image from BGR to RGB
    image = np.array(image.convert('RGB'))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Correct path to the Haar Cascade file
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image, faces

def main():
    st.title("Face Detection App")
    st.write("Upload an image to detect faces.")

    # Upload the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert the file to an OpenCV image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("")
        st.write("Detecting faces...")
        
        # Perform face detection
        result_img, faces = detect_faces(image)
        
        # Display the output
        st.image(result_img, caption='Image with detected faces', use_column_width=True)
        st.success(f"Found {len(faces)} face(s).")

if __name__ == "__main__":
    main()