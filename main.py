import pyttsx3
import speech_recognition as sr
import vlc
import time
import pygame

p = vlc.MediaPlayer("everydaybro.mp4/")
r = sr.Recognizer


p.play()

time.sleep(60)