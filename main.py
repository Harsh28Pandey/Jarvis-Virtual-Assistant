import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pygame
# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""

def speak(text):
    engine.say(text)
    engine.runAndWait()



# def speak(text):
#     tts = gTTS(text)
#     tts.save("temp.mp3")

#     # Intialize Pygame mixer
#     pygame.mixer.init()

#     # Load the saved mp3 file
#     pygame.mixer.music.load("temp.mp3")

#     # Play the loaded mp3 file
#     pygame.mixer.music.play()

#     # Keep the program running until the music stops playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     pygame.mixer.music.unload()
#     os.remove("temp.mp3")




# def aiProcess(command):
#     client = OpenAI(
#     api_key="",
#     )

#     completion = client.chat.completions.create(
#         model="gpt-3.0-turbo",
#         messages=[
#             {"role": "system", "content": "You are a Virtual assistant named Jarvis skilled in general taska like Alexa and Google Cloud Give short responses please"},
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     )

#     return completion.choices[0].message.content




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





    # elif "news" in c.lower():
    #     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={newsapi}")
    #     if r.status_code == 200:
    #         # Parse the JSON reponse
    #         data = r.json()

    #         # Extract the articles
    #         articles = data.get('articles', [])

    #         # Print the headlines
    #         for article in articles:
    #             speak(article['title'])


    # else:
    #     # Let OpenAI handle the request
    #     output = aiProcess(c)
    #     speak(output)





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