import pyttsx3
import speech_recognition as sr
import vlc

p = vlc.MediaPlayer
r = sr.Recognizer

engine = pyttsx3.init()

engine.say("jake paul is number one")

engine.runAndWait()