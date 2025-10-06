import streamlit as st
import cv2
import time
import smtplib
import ssl
from email.message import EmailMessage
from ultralytics import YOLO
import os
from dotenv import load_dotenv


# ================== CONFIG ==================
# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # small, fast model

# Email Setup (replace with real credentials or .env variables)
load_dotenv()

EMAIL_SENDER = os.getenv("sndr")
EMAIL_PASSWORD = os.getenv("pswrd")
EMAIL_RECEIVER = os.getenv("rcvr")


# ================== EMAIL FUNCTION ==================
def send_email(image_path):
    msg = EmailMessage()
    msg['Subject'] = '⚠ Object Detected by Camera'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content("An object was detected by the camera. Picture is attached.")

    with open(image_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(image_path)

    msg.add_attachment(file_data, maintype='image', subtype='jpg', filename=file_name)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

# ================== STREAMLIT APP ==================
st.set_page_config(page_title="Security System", layout="wide")
st.title("Smart Security System with Email Alerts")

# Session state to control start/stop
if "run" not in st.session_state:
    st.session_state.run = False

col1, col2 = st.columns(2)
with col1:
    if st.button("Start Camera"):
        st.session_state.run = True
with col2:
    if st.button("Stop Camera"):
        st.session_state.run = False

# Camera feed window
FRAME_WINDOW = st.image([])

# Start camera
cap = cv2.VideoCapture(0)

last_sent_time = 0  # prevent email flooding

while st.session_state.run:
    ret, frame = cap.read()
    if not ret:
        st.error("Could not access camera.")
        break

    # Run YOLO detection
    results = model(frame, stream=True)

    object_detected = False
    for r in results:
        if len(r.boxes) > 0:
            object_detected = True
            break

    if object_detected:
        current_time = time.time()
        if current_time - last_sent_time > 5:  # send every 5 sec max
            img_name = f"capture_{int(current_time)}.jpg"
            cv2.imwrite(img_name, frame)
            send_email(img_name)
            st.warning("⚠ Object detected! Email sent.")
            last_sent_time = current_time

    # Show live video in Streamlit
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

cap.release()
FRAME_WINDOW.empty()
