
import cv2
import subprocess
    # bec here 2 option is given with web-interface and without web-interface
    
def simple_python():
    # Lib: OpenCV:-> Work with video or images, and apply various image processing techniques
    # Final code
    import cv2

    # Open the camera
    picture_cap = cv2.VideoCapture(0)

    # Correct path to the Haar Cascade file
    face_de = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # When I press a particular key, the camera will turn off
    while True:
        ret, picture_data = picture_cap.read()
        if not ret:
            print("Failed to capture image")
            break

        color = cv2.cvtColor(picture_data, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_de.detectMultiScale(
            color,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(picture_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("camera_Live", picture_data)

        # For closing the camera
        if cv2.waitKey(10) == ord("a"):
            break

    # Release the camera and close all windows
    picture_cap.release()
    cv2.destroyAllWindows()


# Streamlit logic write in Streamlit.py  so user select this then this file excuted in my language 
def streamlit_app():
    subprocess.run(["streamlit", "run", "Streamlit.py"])

def main():
    choice = input("Enter 'python-simple' to run the  python app or 'streamlit' to run the Streamlit app Enter Any one : ").strip().lower()
    if choice == 'python-simple':
        simple_python()
    elif choice == 'streamlit':
        streamlit_app()
    else:
        print("Invalid choice. Please enter 'python-simple' or 'streamlit'.")

if __name__ == "__main__":
    main()