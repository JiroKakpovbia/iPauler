import pyttsx3
import speech_recognition as sr

import time
import os
import sys
#os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ['DISPLAY'] = ': 0.0'
import sdl2


sdl2.SDL_Init()



X = 640
Y = 480

scrn = sdl2.ext.Window((X, Y))


run = True
imp = sdl2.sdlimage.IMG_Load("boxer.jpg").ConvertSurface()
scrn.blit(imp, (0, 0))
scrn.refresh()
while (run):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in sdl2.SDL_PollEvent():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == sdl2.sdlttf.TTF_Quit():
            status = False
 
    
 
# paint screen one time

