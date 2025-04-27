# **Speech Lab IOT**

An intelligent IoT automation system for lab environments powered by offline-first speech control and online real-time synchronization with Firebase.
Designed for reliability, privacy, and seamless operation — even without internet!


---

✨ Features

Offline Speech Control: Fully operational via local voice commands when internet is unavailable.

Real-Time Cloud Sync (When Online): Sync appliance states to Firebase Realtime Database for remote monitoring/control.

Automatic Mode Switching: Seamlessly transitions between offline-only and online-connected modes based on internet availability.

Edge Computing: Speech processing is fully local — no audio is sent externally.

Optimized for Raspberry Pi: Lightweight and efficient for resource-constrained environments.



---

🛠 Tools and Technologies

Picovoice Porcupine (hey_cera.ppn): Wake word detection ("Hey Cera") model.

Picovoice Rhino (cera_cmds.rhn): Speech-to-intent parsing for voice command recognition.

Firebase Realtime Database: Cloud backend for appliance state synchronization (when online).

Raspberry Pi: Central IoT controller managing GPIO operations and speech processing.



---

📂 Directory Structure
```plain text

Speech_Lab_IOT/
│
└── pi/
    ├── main.py             # Main execution script
    ├── speech_engine.py    # Handles wake word detection and speech-to-intent parsing
    ├── cloud.py            # Firebase real-time database integration (only when online)
    ├── gpios.py            # GPIO control for appliances (lights, fans, etc.)
    ├── hey_cera.ppn        # Custom wake word model ("Hey Cera") for Porcupine
    ├── cera_cmds.rhn       # Rhino command set for parsing lab appliance commands

```
---

🚀 Setup Instructions

1. Hardware Requirements

Raspberry Pi 3/4 (with Raspbian OS)

Microphone (USB or Pi-compatible)

Connected appliances via GPIO (Relays, Lights, Fans, etc.)

Internet access (optional — for Firebase syncing)


2. Install Dependencies

SSH into your Raspberry Pi or open a terminal.

``` plain text

sudo apt-get update
sudo apt-get install python3-pip
python3 -m venv speech
source speech/bin/activate
pip install -r requirements.txt

```
---

3. Setup Firebase (Optional)

> Required only if you want online real-time synchronization.



Create a Firebase project.

Enable Realtime Database (start in test mode).

Download your Firebase Admin SDK JSON key.

Save it inside the pi/ folder as firebase_key.json.

Update the cloud.py file if necessary to match your database URL.



---

4. Configure Environment Variables

Create a .env file (optional) if you prefer managing API keys or environment configs separately.


---

5. Run the System

Navigate to the pi/ directory and run:

cd Speech_Lab_IOT/pi
python3 main.py

The system starts listening for "Hey Cera" wake word.

Recognizes speech commands to control lab appliances.

When online, synchronizes appliance states with Firebase.

When offline, automatically operates using only local speech controls without interruption.



---

🗣 Example Commands

After saying "Hey Cera", you can issue commands like:

"Turn on the fan"

"Switch off the light"

"Turn on all devices"

"Turn off the fan"


(Complete list of intents defined in cera_cmds.rhn.)


---

📊 Benchmark & Performance

> (Insert Figures/Graphs showing Rhino Intent Recognition Accuracy, CPU Load, etc.)



Rhino provides high speech-to-intent recognition accuracy even in noisy environments.

Extremely lightweight — minimal CPU usage on Raspberry Pi.

Real-time responsiveness for controlling devices.



---

💡 Future Improvements

Add a web dashboard for remote monitoring and control

Integrate a local MQTT server for faster device messaging

Extend the system to include HVAC, security, and environmental sensors



---

📜 License

This project is licensed under the MIT License.


---

🛡 Badges

   


---

