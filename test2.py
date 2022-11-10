import speech_recognition as sr
import pyttsx3
import os

import vlc
# for text-to-speech
from gtts import gTTS

# for language model
#import transformers
from playsound import playsound

import threading
import time

# for data
import datetime
import numpy as np

import recording
import responses



# Building the AI
class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
        self.awake = False
        self.mood = 1

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic, sr.AudioFile("input.wav") as source:
            print("Listening...")
            audio = recognizer.record(source) 
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
        vlc.MediaPlayer("res.mp3").play  #if you are using mac->afplay or else for windows->start
        #os.system("close res.mp3")
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
    #nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    #os.environ["TOKENIZERS_PARALLELISM"] = "true"
    
    ex=True
    while ex:
        activation = input("Talk to jake? y/n: ")
        if activation == "y":
            thread = threading.Thread(target=recording.record)
            thread.start()
            thread.join()
            ai.speech_to_text()

            result = responses.respond(ai.mood, ai.text)
            os.remove("input.wav")
            if result == 0:
                ai.text_to_speech(np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"]))
                ex = False
                break
            ai.text_to_speech(result)

 

