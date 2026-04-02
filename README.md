# 🤖 J.A.R.V.I.S — AI Voice Assistant

> **Just A Rather Very Intelligent System**  
> A Python-powered personal voice assistant inspired by Tony Stark's JARVIS — built to automate daily tasks, control your environment, and respond to natural voice commands.

---

## 🧠 Overview

JARVIS is a fully voice-activated Python assistant that handles a wide range of real-world tasks — from setting alarms and running automations to speed testing, focus mode, games, and WhatsApp messaging — all triggered by voice commands.

Built as a modular, production-ready personal assistant and a real-world Python portfolio project, each feature lives in its own dedicated module, making the codebase clean, extensible, and easy to demo.

---

## ✨ Features

| Module | Feature |
|---|---|
| `alarm.py` | 🔔 Set and trigger voice alarms |
| `Automation.py` | ⚙️ Automate system-level tasks |
| `Cal.py` | 📅 Calendar & date queries |
| `Calculatenumbers.py` | 🔢 Voice-driven calculator |
| `calls.py` | 📞 Call management via voice |
| `Dictapp.py` | 📖 Dictionary & word definitions |
| `exit_terminal.py` | 🚪 Shutdown / exit commands |
| `Features.py` | 🧩 Core feature dispatcher |
| `file.py` | 🗂️ File management operations |
| `FocusMode.py` | 🎯 Focus/productivity mode |
| `FocusGraph.py` | 📊 Focus session visualizer |
| `game.py` | 🎮 Built-in voice games |
| `GreetMe.py` | 👋 Personalized greeting on startup |
| `INTRO.py` | 🎬 JARVIS intro sequence |
| `Jarvis_main.py` | 🧠 Main entry point & command loop |
| `jarvis_speed.py` | 🌐 Internet speed test |
| `keyboard.py` | ⌨️ Keyboard automation |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Voice I/O:** `speech_recognition`, `pyttsx3`, `pyaudio`
- **Automation:** `pyautogui`, `keyboard`
- **Web & Messaging:** `pywhatkit`, `webbrowser`
- **Weather:** OpenWeatherMap REST API
- **Translation:** `googletrans`
- **Speed Test:** `speedtest-cli`
- **Scheduling:** `datetime`, `time`
- **Packaging:** PyInstaller

---

## 📁 Project Structure

```
AI-Voice-Assistant-Jarvis/
└── Jarvis Project/
    ├── Jarvis_main.py        # 🧠 Main entry — wake word loop & command dispatcher
    ├── Features.py           # 🧩 Core feature router
    ├── INTRO.py              # 🎬 Startup intro sequence
    ├── GreetMe.py            # 👋 Personalized greeting
    ├── alarm.py              # 🔔 Alarm system
    ├── Automation.py         # ⚙️ System automation
    ├── Cal.py                # 📅 Calendar queries
    ├── Calculatenumbers.py   # 🔢 Voice calculator
    ├── calls.py              # 📞 Call handling
    ├── Dictapp.py            # 📖 Dictionary lookup
    ├── exit_terminal.py      # 🚪 Exit/shutdown handler
    ├── file.py               # 🗂️ File operations
    ├── FocusMode.py          # 🎯 Focus/productivity mode
    ├── FocusGraph.py         # 📊 Focus session graph
    ├── game.py               # 🎮 Voice-controlled game
    ├── jarvis_speed.py       # 🌐 Internet speed test
    ├── keyboard.py           # ⌨️ Keyboard automation
    ├── Installer.py          # 📦 Dependency installer
    ├── requirements.txt      # 📋 All dependencies
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
cd "AI-Voice-Assistant-Jarvis/Jarvis Project"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or run the built-in installer:

```bash
python Installer.py
```

> **Note:** If you hit issues with `pyaudio` on Windows:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### 3. Set up API keys

Create a `.env` file in the project folder:

```env
OPENWEATHER_API_KEY=your_openweathermap_api_key_here
```

Get a free key at [openweathermap.org](https://openweathermap.org/api)

### 4. Run JARVIS

```bash
python Jarvis_main.py
```

Speak to JARVIS after the intro — it's listening!

---

## 🗣️ Example Commands

```
"JARVIS, set an alarm for 7 AM"
"JARVIS, what's the weather in Hyderabad?"
"JARVIS, send a WhatsApp message to Mom"
"JARVIS, play Blinding Lights on YouTube"
"JARVIS, translate hello to Hindi"
"JARVIS, what is the speed of my internet?"
"JARVIS, start focus mode"
"JARVIS, define serendipity"
"JARVIS, calculate 25 multiplied by 4"
"JARVIS, let's play a game"
```

---

## 📦 Dependencies

```
speechrecognition
pyttsx3
pyaudio
pywhatkit
requests
googletrans==4.0.0-rc1
speedtest-cli
pyautogui
keyboard
python-dotenv
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔮 Roadmap

- [ ] Always-on wake word detection (no button press needed)
- [ ] GUI dashboard with real-time command display
- [ ] Smart home / IoT device integration
- [ ] Multilingual voice support (Hindi, Telugu)
- [ ] Automotive integration — navigation & music adaptation *(TATA Motors target)*
- [ ] Emotion-aware response tuning

---

## 🏆 Highlights

- 🏅 Submitted to **TATA Innovation Challenge 2025** as part of *AI Co-Pilot: Revolutionizing Driver Safety*
- 🧩 Fully modular architecture — each feature is a standalone, independently testable module
- ⚙️ Ships with `Installer.py` for zero-friction onboarding
- 📦 PyInstaller-ready for standalone `.exe` distribution

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Naseer**  
AWS Cloud Engnieer | Python | DevOps  
[GitHub](https://github.com/Naseer1907) · [LinkedIn](https://linkedin.com/in/naseer1907)

---

> *"Sometimes you gotta run before you can walk."* — Tony Stark