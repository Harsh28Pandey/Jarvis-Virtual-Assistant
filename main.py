import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pygame
import os

# pip install pygame
# pip install pocketsphinx
# pip install pyttsx3
# pip install pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Your_API_KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if("open google" in c.lower()):
        webbrowser.open("https://www.google.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://www.youtube.com")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://www.facebook.com")
    elif("open instagram" in c.lower()):
        webbrowser.open("https://www.instagram.com")
    elif("open linkedin" in c.lower()):
        webbrowser.open("https://www.linkedin.com")
    elif("open whatsapp" in c.lower()):
        webbrowser.open("https://www.whatsapp.com")
    elif(c.lower().startswith("play")):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Jarvis Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Jarvis Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah, may I help you?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            speak("Voice Cannot be clear, {0}".format(e))
