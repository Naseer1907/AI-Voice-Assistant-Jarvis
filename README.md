# 🤖 J.A.R.V.I.S — AI Voice Assistant

> **Just A Rather Very Intelligent System**  
> A Python-powered personal voice assistant inspired by Tony Stark's JARVIS — built to automate daily tasks, control your environment, and respond to natural voice commands.

---

## 🧠 Overview

JARVIS is a fully offline-capable, voice-activated Python assistant that handles a wide range of tasks — from sending WhatsApp messages and fetching live weather to playing YouTube videos and translating languages — all triggered by a single wake word.

Built as a production-ready personal assistant and a real-world cloud/Python portfolio project, JARVIS is designed with extensibility in mind, making it easy to add new features or integrate with external APIs.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎙️ **Voice Recognition** | Listens for voice commands using `speech_recognition` |
| 🔊 **Text-to-Speech** | Responds with natural speech via `pyttsx3` |
| 📱 **WhatsApp Messaging** | Sends messages hands-free using `pywhatkit` |
| 🌦️ **Live Weather** | Fetches real-time weather data via OpenWeatherMap API |
| ▶️ **YouTube Playback** | Plays any YouTube video on voice command |
| 🔍 **Google Search** | Launches browser searches instantly |
| 🌐 **Language Translation** | Translates text across multiple languages |
| ⏰ **Reminders** | Sets and manages time-based reminders |
| 🌐 **Internet Speed Check** | Runs a live speed test on demand |
| 🕐 **Date & Time** | Tells current time and date |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Voice I/O:** `speech_recognition`, `pyttsx3`, `pyaudio`
- **Messaging:** `pywhatkit`
- **Weather:** OpenWeatherMap REST API
- **Translation:** `googletrans`
- **Speed Test:** `speedtest-cli`
- **Web Control:** `webbrowser`, `pywhatkit`
- **Scheduling:** `datetime`, `time`

---

## 📁 Project Structure

```
AI-Voice-Assistant-Jarvis/
├── jarvis.py            # Main entry point — wake word loop & command dispatcher
├── features/
│   ├── weather.py       # OpenWeatherMap API integration
│   ├── whatsapp.py      # WhatsApp messaging via pywhatkit
│   ├── youtube.py       # YouTube playback
│   ├── translator.py    # Language translation
│   ├── reminder.py      # Reminder scheduling
│   └── speedtest.py     # Internet speed check
├── utils/
│   ├── speak.py         # TTS helper (pyttsx3)
│   └── listen.py        # Speech recognition helper
├── requirements.txt     # All dependencies
├── .env.example         # Template for API keys
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A working microphone
- Internet connection (for weather, WhatsApp, YouTube, translation)

### 1. Clone the repository

```bash
git clone https://github.com/Naseer1907/AI-Voice-Assistant-Jarvis.git
cd AI-Voice-Assistant-Jarvis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If you encounter issues with `pyaudio` on Windows, install it via:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### 3. Set up your API keys

Copy the example env file and add your keys:

```bash
cp .env.example .env
```

Then edit `.env`:

```env
OPENWEATHER_API_KEY=your_openweathermap_api_key_here
```

Get your free key at [openweathermap.org](https://openweathermap.org/api)

### 4. Run JARVIS

```bash
python jarvis.py
```

Say **"Hey JARVIS"** to wake the assistant, then give a command.

---

## 🗣️ Example Commands

```
"Hey JARVIS, what's the weather in Hyderabad?"
"Hey JARVIS, send a WhatsApp message to Mom"
"Hey JARVIS, play Blinding Lights on YouTube"
"Hey JARVIS, translate hello to Spanish"
"Hey JARVIS, set a reminder for 6 PM"
"Hey JARVIS, search Python tutorials on Google"
"Hey JARVIS, what's the internet speed?"
"Hey JARVIS, what time is it?"
```

---

## 📦 Requirements

```
speechrecognition
pyttsx3
pyaudio
pywhatkit
requests
googletrans==4.0.0-rc1
speedtest-cli
python-dotenv
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔮 Roadmap

- [ ] Wake-word detection without button press (always-on mode)
- [ ] GUI dashboard with real-time command display
- [ ] Smart home integration (IoT device control)
- [ ] Multilingual voice support (Hindi, Telugu)
- [ ] Automotive integration — navigation & music adaptation (TATA Motors collaboration target)
- [ ] Emotion-aware response tuning

---

## 🏆 Highlights

- Submitted to **TATA Innovation Challenge 2025** as part of the *AI Co-Pilot: Revolutionizing Driver Safety* project
- Designed with a modular architecture to support plug-and-play feature extensions
- Handles real-world API integrations with error fallback and retry logic

---

## 🤝 Contributing

Pull requests are welcome! For major feature additions, please open an issue first to discuss the approach.

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

---


---

## 👨‍💻 Author

**Naseer**  
Cloud Enginner · AWS | Python | DevOps  
[GitHub](https://github.com/Naseer1907) · [LinkedIn](https://linkedin.com/in/naseer1907)

---

> *"Sometimes you gotta run before you can walk."* — Tony Stark