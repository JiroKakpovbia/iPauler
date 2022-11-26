import pygame
import os
import subprocess
import time
import json
#subprocess.call(crop, shell=True)

pygame.init()
pygame.mixer.init()

X = 480
Y = 320

    
screen = pygame.display.set_mode((X, Y))

result = pygame.mixer.music.load("meme.mp3")
A = pygame.image.load("mouth/A.png").convert()
B = pygame.image.load("mouth/B.png").convert()
C = pygame.image.load("mouth/C.png").convert()
D = pygame.image.load("mouth/D.png").convert()
E = pygame.image.load("mouth/E.png").convert()
F = pygame.image.load("mouth/F.png").convert()
G = pygame.image.load("mouth/G.png").convert()
H = pygame.image.load("mouth/H.png").convert()
X = pygame.image.load("mouth/X.png").convert()

os.system ("/home/se101/rhubarb-lip-sync/rhubarb/rhubarb -o output.json -f json -r pocketSphinx meme.wav")

f = open('output.json')
  
timing = json.load(f)
  
  


pygame.mixer.music.play()
start = time.time()
value = 0
while pygame.mixer.music.get_busy():

    for i in timing['mouthCues']:
        while i['start'] < start:
            pass
        print(i['value'])
        screen.blit(exec(i['value']), (0, 0))

f.close()
end = time.time()
pygame.mixer.music.unload()
os.remove("output.json")