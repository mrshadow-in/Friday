from Brain.brain import ReplyBrain
from Body.listen import MicConnect
from Body.speak import Speak
from Features.clap import Tester
from Features.wakeup import wakeupDetected
from Brain.taskexe import taskexe

def MainExecution():
    
    Speak("JARVIS has been Initialized and Ready to Use")
    while True:
        Data = MicConnect()
        #Data = "open instagram"
        Data= str(Data).replace(".","")
        ValueReturned = False
        if len(Data) < 1:  # Check if Data contains less than 1 word
            pass  # Skip to the next iteration if condition is met
        else:
            ValueReturned = taskexe(Data)

        if ValueReturned==True:
            pass
        elif Data == "":
            pass
        elif Data == "Bye":
            Speak("Stoping Systems")
            break
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)