import pyaudio
import pyautogui as pui
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            pui.typewrite(text)
            print(text)
            engine.say(text)
            engine.runAndWait()
        except:
            pass