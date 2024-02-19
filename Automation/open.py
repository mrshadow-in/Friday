import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from Body.speak import Speak
def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        neoweb = Query.replace("visit ", "").replace("launch ", "")
        link = f"https://{neoweb}.com"
        webbrowser.open(link)
        Speak(f"Visiting {neoweb}")
    elif "launch" in Query:
        neoweb = Query.replace("visit ", "").replace("launch ", "")
        link = f"https://{neoweb}.com"
        webbrowser.open(link)
        Speak(f"Launching {neoweb}")

    elif "open" in Query:
        neoapp = Query.replace("open ","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(neoapp)
        sleep(1)
        keyboard.press("enter")
        sleep(1)
        Speak(f"Opening {neoapp}")
        return True
    
    elif "start" in Query:
        neoapp = Query.replace("start ","")
        pyautogui.press("win")
        sleep(1)
        keyboard.write(neoapp)
        sleep(1)
        keyboard.press("enter")
        sleep(0.5)
        Speak(f"Starting {neoapp}")
        return True

    