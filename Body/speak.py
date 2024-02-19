import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',135)
    print("")
    print(f'J.A.R.V.I.S :{Text}.')
    print("")
    engine.say(Text)
    engine.runAndWait()
