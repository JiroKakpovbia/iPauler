# for speech-to-text
import speech_recognition as sr

# for text-to-speech
from gtts import gTTS

# for language model
import transformers

import os
import time
import random

# for data
import os
import datetime
import numpy as np


# Building the AI
class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
        self.awake = False
        self.mood = 1

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = recognizer.listen(mic)
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Input  --> ", self.text)
        except:
            print("Input  -->  ERROR")
            

    @staticmethod
    def text_to_speech(text):
        print("Jake Paul --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)

        speaker.save("res.mp3")
        statbuf = os.stat("res.mp3")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200
        os.system('start res.mp3')  #if you are using mac->afplay or else for windows->start
        # os.system("close res.mp3")
        time.sleep(int(50*duration))
        os.remove("res.mp3")
        
        

    def wake_up(self, text):
        return True if self.name in text else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Running the AI
if __name__ == "__main__":
    
    ai = ChatBot(name="Jake Paul")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    
    ex=True
    while ex:
        ai.speech_to_text()

        ##Only respond if awake
        if ai.awake:

            if ai.mood == 1:

                ## change to mood 2
                if "mood two" in ai.text:
                    res = "Now in mood two."
                    ai.mood = 2

                ## change to mood 3
                elif "mood three" in ai.text:
                    res = "Now in mood three."
                    ai.mood = 3

                ##flip a coin
                elif "flip a coin" in ai.text:
                    if random.randrange(2) == 0:
                        res = "Heads"
                    else:
                        res = "Tails"
                    
                ## play rock paper scissors
                elif "rock paper scissors" in ai.text:
                    value = random.randrange(3)
                    if value == 0:
                        res = "Rock, Paper, Scissors. Rock!"
                    elif value == 1:
                        res = "Rock, Paper, Scissors. Paper!"
                    else:
                        res = "Rock, Paper, Scissors. Scissors!"
                
                ## action time
                elif "time" in ai.text:
                    res = ai.action_time()
                  
                ## what day
                elif "what day" in ai.text:
                    res = "It's every day bro!"

                ## city
                elif "city" in ai.text:
                    res = "England is my city."

                ## number one
                elif "number one" in ai.text:
                    res = "I'm number one."

                ## how old
                elif "how old" in ai.text:
                    res = "I'm twenty five years old."

                ## boxing record
                elif "record" in ai.text:
                    res = "Six and O baby. Hear that? Six and O."

                ## best YouTube boxer
                elif "best YouTube boxer" in ai.text:
                    res = "Realy? Really? It's me you dumbass. Don't ask me that again."

                ## your name
                elif "your name" in ai.text:
                    res = "I'm the one and only Jake Joseph Paul."
                
                ## respond politely
                elif any(i in ai.text for i in ["thank","thanks"]):
                    res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","mention not"])
            
                else:
                    if ai.text=="ERROR":
                        res="Sorry, come again?"

##            elif ai.mood == 2:
##                
##                ## change to mood 1
##                if "mood one" in ai.text:
##                    res = "Now in mood one."
##                    ai.mood = 1
##
##                ## change to mood 3
##                elif "mood three" in ai.text:
##                    res = "Now in mood three."
##                    ai.mood = 3

##            elif ai.mood == 3:
##                ## change to mood 1
##                if "mood one" in ai.text:
##                    res = "Now in mood one."
##                    ai.mood = 1
##
##                ## change to mood 2
##                elif "mood two" in ai.text:
##                    res = "Now in mood two."
##                    ai.mood = 2

            ##Stop running the program if certain keyword is said
            if any(i in ai.text for i in ["exit","close"]):
                res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
                
                ex=False

            ## conversation
            else:   
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()

            ai.text_to_speech(res)


        ## wake up if name inputted
        if ai.name in ai.text:
        
            res = "Jake Paul is here and ready to rumble"
            ai.awake = True
            ai.text_to_speech(res)

    print("----- Closing down Jake Paul -----")
