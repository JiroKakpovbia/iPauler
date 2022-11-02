import pyttsx3
import speech_recognition as sr
import vlc
import time
import pygame

p = vlc.MediaPlayer("everydaybro.mp4/")
r = sr.Recognizer

pygame.init()
X = 600
Y = 600

scrn = pygame.display.set_mode((X, Y))

img = pygame.image.load("boxer.JPG").convert()

scrn.blit(img, (0, 0))
pygame.display.flip()

engine = pyttsx3.init()

engine.say("jake paul is number one")

engine.runAndWait()

p.play()

time.sleep(60)