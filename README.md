#  Smart Security System with Email Alerts

AI-powered security camera that detects objects and sends instant email notifications with captured images.


##  What It Does

- **Real-time Detection**: Uses YOLOv8 AI to detect objects via webcam
- **Instant Alerts**: Sends email with captured image when objects detected
- **Live Feed**: Displays camera feed in web browser
- **Smart Throttling**: Prevents email spam (5-second cooldown)

---

##  Quick Start

### 1. Install Dependencies
```bash
pip install streamlit opencv-python ultralytics python-dotenv
```

### 2. Setup Email Credentials

Create `.env` file:
```env
sndr=your_email@gmail.com
pswrd=your_app_password
rcvr=receiver_email@gmail.com
```

**Get Gmail App Password**: [Google Account Settings](https://myaccount.google.com/apppasswords)

### 3. Run Application
```bash
streamlit run app.py
```

### 4. Use the System
- Click **"Start Camera"** to begin monitoring
- Click **"Stop Camera"** to end session
- Emails sent automatically when objects detected

---

##  How It Works

```
Webcam → YOLOv8 Detection → Object Found? → Capture Image → Send Email
                                    ↓
                              Live Stream Display
```

### Technical Flow
1. **Camera Access**: OpenCV captures video frames
2. **AI Detection**: YOLOv8 analyzes each frame for objects
3. **Smart Alerts**: When detected, saves image and emails it
4. **Cooldown**: 5-second delay prevents spam
5. **Display**: Real-time feed shown in Streamlit interface

---

##  Project Structure

```
security-system/
├── app.py              # Main application
├── .env                # Email credentials (create this)
├── yolov8n.pt          # AI model (auto-downloaded)
├── requirements.txt    # Dependencies
└── capture_*.jpg       # Captured images (auto-generated)
```

---

## 🔧 Key Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **UI** | Streamlit | Web interface with start/stop controls |
| **AI Detection** | YOLOv8 | Real-time object detection |
| **Camera** | OpenCV | Video capture and frame processing |
| **Email** | SMTP (Gmail) | Send alerts with attachments |
| **Config** | python-dotenv | Secure credential management |

---

##  Requirements

```txt
streamlit==1.28.0
opencv-python==4.8.0
ultralytics==8.0.0
python-dotenv==1.0.0
```

### Deploy Online
```bash
# Using Streamlit Cloud (requires internet camera access)
streamlit run app.py --server.enableCORS=false
```

##  Security Notes

-  Never commit `.env` file to Git
-  Use Gmail App Passwords (not account password)
-  Enable 2-Factor Authentication on Gmail
-  Add `.env` to `.gitignore`
-  Captured images stored locally (auto-cleanup recommended)


##  Use Cases

- **Home Security**: Monitor entry points
- **Office Surveillance**: Track after-hours activity
- **Wildlife Monitoring**: Capture animal movements
- **Baby Monitor**: Alert when baby wakes
- **Package Detection**: Know when deliveries arrive
- **Pet Monitoring**: Check on pets remotely


<p align="center">
  <strong>Made with 🔒 for Smart Security</strong><br>
  <sub>Powered by YOLOv8 & Streamlit</sub>
</p>