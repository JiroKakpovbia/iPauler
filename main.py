import speech_recognition as sr
import pyttsx3
import os

import vlc
# for text-to-speech
from gtts import gTTS

# for language model

from playsound import playsound

import threading
import time

# for data
import datetime
import numpy as np

import recording
import responses

import pygame

import pvporcupine

from pvrecorder import PvRecorder

p = vlc.MediaPlayer("everydaybro.mp4/")
<<<<<<< HEAD
=======
vlc.MediaPlayer().video_set_scale(0.6)
>>>>>>> fd3c96a03c34c3ad850923f2bba692ab58d4f24d

access_key = "KrtyFBDP3S9uW20iiBF0l0QarTeLnJx7hIgT8noopQrXFfqTOCrhTg=="
#keyword_paths = ['/wakeword']
#handle = pvporcupine.create(access_key=access_key, keyword_paths=keyword_paths)
#handle = pvporcupine.create(access_key=access_key, keywords=['picovoice'])



# Building the AI
class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name
        self.awake = False
        self.mood = 1

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.AudioFile("input.wav") as source:
            audio = recognizer.record(source) 
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
            print("Input  --> ", self.text)
        except:
            print("Input  -->  ERROR")

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Say 'Jake Paul'...")
            audio = recognizer.listen(mic)
            self.text="ERROR"
        try:
            self.text = recognizer.recognize_google(audio)
        except:
            self.text="ERROR"

    def get_next_audio_frame(self):
        pass

    def wakeword(self):
        ppn = pvporcupine.create(access_key=access_key, keywords=['alexa', 'jarvis'])
        keyword_index = ppn.process(get_next_audio_frame())
        if keyword_index >= 0:
            ai.awake = True
        recorder = PvRecorder(device_index=-1)
        recorder.start()

        pcm = recorder.read()
        ppn.process(pcm)

    @staticmethod
    def text_to_speech(text):
        print("Jake Paul --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)

        speaker.save("res.mp3")
        statbuf = os.stat("res.mp3")
        mbytes = statbuf.st_size / 1024
        duration = mbytes / 200
        result = pygame.mixer.music.load("res.mp3")
        pygame.mixer.music.play()
        open = pygame.image.load("mouth/m4.png").convert()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(500)
            screen.blit(open, (0, 0))
            pygame.display.flip()
            pygame.time.wait(500)
            screen.blit(m1, (0, 0))
            pygame.display.flip()
        screen.blit(m1, (0, 0))
        pygame.mixer.music.unload()
        os.remove("res.mp3")

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Running the AI
if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    X = 480
    Y = 320

    
    devices = PvRecorder.get_audio_devices()
    print(devices)
    screen = pygame.display.set_mode((X, Y))
    m1 = pygame.image.load("mouth/m1.png").convert()
    screen.blit(m1, (0, 0))
    
    pygame.display.flip()

    ai = ChatBot(name="Jake Paul")

    WAKE = "Jake Paul"

    ex=True

    while ex:

        if ai.awake:     

            ai.awake = False  
        
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
            elif result == 1:
                p.play()
                while not "stop" in ai.text:
                    ai.listen()
                p.stop()
                screen.blit(m1, (0, 0))

                
            else: ai.text_to_speech(result)
            
        else: 
            ai.listen()

        if ai.name in ai.text:
            pygame.mixer.music.load("discord.mp3")
            pygame.mixer.music.play()
            ai.awake = True


 

