import os
import random
import datetime
import numpy as np
import time
import vlc

from functions import getweather as getweather
from functions import getlocation as getlocation




p = vlc.MediaPlayer("everydaybro.mp4/")


def respond(mood, input):

    if mood == 1:

        res = "Sorry, don't care"

        ## change to mood 2
        if "mood two" in input:
            res = "Now in mood two."
            mood = 2

        ## change to mood 3
        elif "mood three" in input:
            res = "Now in mood three."
            mood = 3

        ##flip a coin
        elif "flip a coin" in input:
            if random.randrange(2) == 0:
                res = "Heads"
            else:
                res = "Tails"
            
        ## play rock paper scissors
        elif "rock paper scissors" in input:
            value = random.randrange(3)
            if value == 0:
                res = "Rock, Paper, Scissors. Rock!"
            elif value == 1:
                res = "Rock, Paper, Scissors. Paper!"
            else:
                res = "Rock, Paper, Scissors. Scissors!"

        elif "weather" in input:

            city = getlocation()

            weather = getweather(city)
            
            res = "The current temperature in "+city+" is "+str((weather[0] - 273.15) * 1.8 + 32)+"farenheight. The current atmospheric pressure is "+str(weather[1])+" hectopascal units. The current humidity is "+str(weather[2])+" percent. The overall conditions are "+str(weather[3])

            if weather == 0:
                res = "The weather is very nice"

        
        ## action time
        #elif "time" in input:
            #res = ai.action_time()
            
        ## what day
        elif "what day" in input:
            res = "It's every day bro!"

        elif "music" in input:
            p.play()
            time.sleep(60)

        ## city
        elif "city" in input:
            res = "England is my city."

        ## number one
        elif "number one" in input:
            res = "I'm number one."

        ## how old
        elif "how old" in input:
            res = "I'm twenty five years old."

        ## boxing record
        elif "record" in input:
            res = "Six and O baby. Hear that? Six and O."

        ## best YouTube boxer
        elif "best boxer" in input:
            res = "Realy? Really? It's me you dumbass. Don't ask me that again."

        ## your name
        elif "your name" in input:
            res = "I'm the one and only Jake Joseph Paul."
        
        ## respond politely
        elif any(i in input for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])

        else:
            if input=="ERROR":
                res="Sorry, come again?"

    if any(i in input for i in ["exit","close"]):
        return 0

    return res


    