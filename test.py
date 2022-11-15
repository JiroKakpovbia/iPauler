import pyttsx3
import speech_recognition as sr

import time
import os
import sys
#os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ['DISPLAY'] = ': 0.0'
import pygame


pygame.init()



X = 640
Y = 480

scrn = pygame.display.set_mode((X, Y))


run = True
imp = pygame.image.load("boxer.jpg").convert()
scrn.blit(imp, (0, 0))
pygame.display.flip()
while (run):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
    
 
# paint screen one time
pygame.display.flip()
