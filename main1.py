import speech_recognition as sr
import spacy
import webbrowser
import datetime
import os
import pyttsx3

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
engine = pyttsx3.init()

def speak(text):
    print("🔊", text)
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("✅ You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("API unavailable or network issue.")
        return ""

def analyze_text(text):
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return doc, entities

def perform_action(text):
    doc, entities = analyze_text(text)

    if "time" in text:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "open" in text:
        for token in doc:
            if token.pos_ == "PROPN" or token.pos_ == "NOUN":
                site = token.text.lower()
                urls = {
                    "google": "https://www.google.com",
                    "youtube": "https://www.youtube.com",
                    "facebook": "https://www.facebook.com",
                    "github": "https://github.com"
                }
                if site in urls:
                    speak(f"Opening {site}")
                    webbrowser.open(urls[site])
                    return
        speak("Sorry, I couldn't find the website.")

    elif "remind" in text or "reminder" in text:
        date_info = entities.get("DATE", "sometime")
        time_info = entities.get("TIME", "")
        speak(f"Reminder set for {date_info} {time_info}. (Note: This is just a demo!)")

        # Save to file (simulate a reminder system)
        with open("reminders.txt", "a") as file:
            file.write(f"Reminder: {text}\n")
        speak("Reminder saved.")

    else:
        speak("Sorry, I don't know how to handle that yet.")

def main():
    speak("Hi! I am your voice assistant. What can I do for you?")
    while True:
        command = get_voice_input()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            perform_action(command)

if __name__ == "__main__":
    main()
