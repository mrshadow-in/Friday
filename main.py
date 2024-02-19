from Body.speak import Speak
from Features.clap import Tester
from Jarvis import MainExecution
def clapdet():
    Speak("Waiting Intialization")
    test = Tester()
    Speak("Stating Intialization")
    if "True" in test:
        MainExecution()
    else:
        pass

import speech_recognition as sr
import os
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")
    except:
        return ""
    query = str(query).lower()
    print(query)
    return query

def wakeupDetected():
    query = listen().lower()

    if "hey jarvis" or "hey jarvis" or "wake up" or "hello jarvis" in query:
        MainExecution()

    else:
        pass

while True:
    clapdet()