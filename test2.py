from subprocess import call
import speech_recognition as sr
#import serial
#import RPi.GPIO as GPIO    
# for speech-to-text
import speech_recognition as sr

# for text-to-speech
from gtts import gTTS

# for language model
import transformers
from playsound import playsound
import pyaudio
import wave
import os
import time

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
            audio = AudioFile("input.wav")
            print(audio)
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
    #nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    #os.environ["TOKENIZERS_PARALLELISM"] = "true"
    
    ex=True
    while ex:
        ai.speech_to_text()

 

