# Voice-Controlled Smart Home Automation (Offline + Realtime Sync)

This project implements an **IoT Smart Home Automation System** using **Raspberry Pi**, **Picovoice** (Porcupine + Rhino), and **Firebase Realtime Database**.  
It enables **offline voice control** of home appliances with **real-time state synchronization** to a remote **web app dashboard** — ensuring both **privacy** and **accessibility**.

---

## ✨ Features

- 🎹 **Offline Wake Word Detection** (using Picovoice Porcupine)
- 🦰 **Offline Speech-to-Intent Parsing** (using Picovoice Rhino)
- ⚡ **Local Appliance Control** (using Raspberry Pi GPIO)
- 🌐 **Realtime Cloud Sync** (Firebase Realtime Database)
- 🛡️ **Edge Computing** (no need for constant Internet access)
- 📊 **Highly Accurate and Efficient** models

---

## 🛠 Tools & Technologies

- Raspberry Pi 3 / 4 (or equivalent)
- Python 3.x
- Picovoice Porcupine SDK
- Picovoice Rhino SDK
- Firebase Realtime Database
- GPIO Zero / RPi.GPIO Python libraries

---

## 📦 Project Structure

```
├── main.py             # Main application file
├── voice_commands.py   # Handles voice capture and intent recognition
├── appliance_control.py# Controls GPIO relays based on commands
├── firebase_sync.py    # Syncs appliance states with Firebase
├── config.py           # Configuration file (API keys, model paths, GPIO pins)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── models/             # Directory for Porcupine and Rhino models
```

---

## ⚙️ Setup Instructions

### 1. Install OS and Prepare Raspberry Pi
- Install **Raspberry Pi OS Lite** (or Desktop).
- Update your Pi:
  ```bash
  sudo apt-get update
  sudo apt-get upgrade
  ```
- Enable **I2C**, **SPI**, and **GPIO** if needed:
  ```bash
  sudo raspi-config
  ```

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/voice-smart-home.git
cd voice-smart-home
```

### 3. Set Up Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Download Picovoice Models
- Create an account at [Picovoice Console](https://console.picovoice.ai/).
- Train and download:
  - **Wake Word** (Porcupine)
  - **Speech-to-Intent** context (Rhino)
- Place downloaded `.ppn` (Porcupine) and `.rhn` (Rhino) model files into the `models/` directory.
- Update their paths in `config.py`.

### 5. Configure Firebase
- Create a Firebase project.
- Set up **Realtime Database**.
- Get your **Service Account JSON** and **Database URL**.
- Add Firebase credentials to `config.py`:
  ```python
  FIREBASE_CREDENTIALS = "path/to/your/serviceAccountKey.json"
  FIREBASE_DATABASE_URL = "https://your-database.firebaseio.com/"
  ```

### 6. Connect Appliances to GPIO
- Wire relays to Raspberry Pi GPIO pins.
- Map each relay in `appliance_control.py`.

Example:
```python
DEVICE_GPIO_MAP = {
    "light": 17,
    "fan": 27,
    "heater": 22
}
```

---

## 🚀 Running the Application

```bash
python main.py
```

The system will:
- Continuously listen for the **wake word**.
- Parse the spoken command into an **intent**.
- **Control the appliance** via GPIO and **update the Firebase** database in real-time.

---

## 🖥️ Web Dashboard (Optional)

You can also set up a **remote web dashboard** connected to the same Firebase database to monitor and manually control appliances from anywhere.

---

## 📊 Performance

| Model | CPU Usage (RPi 3) | Accuracy | Latency |
|:-----:|:-----------------:|:--------:|:-------:|
| Porcupine Wake Word | ~3.8% | 95% | ~50 ms |
| Rhino Intent Parser | ~15-25% | 95%+ | ~150 ms |

*(Tested in moderately noisy environments)*

---

## 👋 Contributions

Feel free to fork the project, improve it, and send a pull request!

---

## 📜 License

This project is licensed under the MIT License.

---

## 🧑‍💻 Acknowledgements

- [Picovoice](https://picovoice.ai/)
- [Firebase](https://firebase.google.com/)
- Raspberry Pi Foundation

