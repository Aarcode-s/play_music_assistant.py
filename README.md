# -play_music_assistant.py
# 🎙️ Voice Assistant in Python

This is a simple voice assistant made with Python. It listens to your command, and when you say **"activate"**, it asks what song you want to hear and plays it on YouTube.

---

## 📦 Features

- Listens for your voice
- Responds with voice
- Plays songs from YouTube when you say "activate"

---

## 🚀 How to Run

### 1. Clone the repository

### 2. Install dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

> ⚠️ If `pyaudio` fails to install on Windows, try:
```bash
pip install pipwin
pipwin install pyaudio
```

### 3. Run the Assistant
```bash
python assistant.py
```

---

## 🗣️ How to Use

1. Say "activate" when prompted.
2. After it responds, say the name of the song.
3. It will play the song on YouTube automatically.

---

## 💻 Dependencies

- `pyttsx3` — for offline voice output
- `speech_recognition` — for voice input
- `pywhatkit` — to open YouTube and search

---

## 🔧 Requirements

- Python 3.7+
- Microphone
- Internet connection (for YouTube & Google APIs)

---

## 🤖 Future Ideas

- Search Google by voice
- Tell the weather
- Tell the time
- Play offline media
- Open desktop apps

