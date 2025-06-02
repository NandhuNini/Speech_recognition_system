
 🗣️ Voice Command Assistant using Speech + spaCy

A simple voice-activated assistant that understands natural speech using **spaCy NLP** and performs real-world actions like opening websites, telling the time, and saving reminders.
 🚀 Features

* 🎤 Converts voice to text using Google Speech API
* 🧠 Uses spaCy for NLP (Named Entity Recognition, intent detection)
* ⏰ Tells current time
* 🌐 Opens websites like YouTube, Google, Facebook, GitHub
* 📝 Saves simple reminders to a local file
* 💬 Responds back using text-to-speech

📂 Project Structure
voice_assistant/
├── main.py               # Main program file
├── reminders.txt         # Stores user reminders (created automatically)
├── requirements.txt      # Python dependencies
└── README.md             # Project description (this file)

 🧰 Requirements

* Python 3.7+
* Microphone for input
* Internet connection (for speech recognition)

Install the dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm

 🛠️ How to Run

1. Clone this repository or download the ZIP:

```bash
git clone https://github.com/your-username/voice-assistant-spacy.git
cd voice-assistant-spacy

2. Run the assistant:

```bash
python main.py
```

3. Start speaking commands like:

   * “What time is it?”
   * “Open YouTube”
   * “Set a reminder for tomorrow at 5 PM”
   * “Exit”

---

### ✅ Example Commands

| Command                         | Response                          |
| ------------------------------- | --------------------------------- |
| “What time is it?”              | Reads out current time            |
| “Open Google”                   | Opens Google in your browser      |
| “Set a reminder for 5 PM today” | Saves reminder to `reminders.txt` |
| “Exit”                          | Closes the assistant              |

 📌 Customization

* Add more actions in the `perform_action()` function.
* Integrate with APIs (weather, to-do apps, alarms).
* Replace spaCy with a transformer for deeper understanding.

---

### 📖 Libraries Used

* [`speechrecognition`](https://pypi.org/project/SpeechRecognition/)
* [`spacy`](https://spacy.io/)
* [`pyttsx3`](https://pypi.org/project/pyttsx3/)
* [`pyaudio`](https://people.csail.mit.edu/hubert/pyaudio/)

---

### 🧠 Future Improvements

* GUI using Streamlit or Tkinter
* Offline speech recognition with Vosk or Whisper
* Reminder alert system with sound notifications
* Voice authentication

