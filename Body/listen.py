import speech_recognition as sr
from googletrans import Translator 

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language="hi")
    except:
        return ""
    query = str(query).lower()
    return query



def TransEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f'You Said: {data} ')
    return data

def MicConnect():
    query1 = listen()
    if query1 != "":
        data1 = TransEng(query1)
        return data1
    else:
        pass
