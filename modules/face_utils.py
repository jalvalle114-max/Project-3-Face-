import face_recognition
import cv2
from PIL import Image

def load_face_encoding_from_image(image_path):
    try:
        img = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) == 0:
            print(f"No faces found in {image_path}")
            return None, None
        return Image.fromarray(img), encodings[0]
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return None, None

def webcam_capture_one_frame():

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return None, None

    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture frame from webcam.")
        return None, None

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_frame)
    if len(encodings) == 0:
        return Image.fromarray(rgb_frame), None
    return Image.fromarray(rgb_frame), encodings[0]
