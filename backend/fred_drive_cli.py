#!/usr/bin/env python3
import os
import sys
import speech_recognition as sr
import subprocess
from drive_utils import list_files, download_file

def speak(text):
    subprocess.run(["say", text])

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak your command:")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("😕 Sorry, I didn’t catch that.")
    except sr.RequestError:
        print("❌ Could not access speech recognition.")
    return None

def handle_command(command):
    if "list" in command.lower():
        files = list_files(limit=10)
        if not files:
            speak("No files found.")
        for f in files:
            line = f"{f['name']} ({f['id']})"
            print(line)
            speak(f["name"])
    elif "download" in command.lower():
        name_to_match = command.split("download", 1)[-1].strip().lower()
        files = list_files(limit=20)
        for f in files:
            if name_to_match in f["name"].lower():
                speak(f"Downloading {f['name']}")
                output_file = f["name"]
                download_file(f["id"], output_file)
                speak(f"{f['name']} downloaded")
                return
        speak("Couldn't find a matching file to download.")
    else:
        speak("Sorry, I didn’t understand that command.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = get_voice_input()

    if prompt:
        print(f"🔍 You said: {prompt}")
        handle_command(prompt)
