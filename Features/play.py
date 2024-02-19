import pywhatkit
def play(Query):

    name = str(Query).replace("play ","")
    import pywhatkit
    pywhatkit.playonyt(Query)
    return True
