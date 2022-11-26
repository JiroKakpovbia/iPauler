import pygame
import os
import subprocess
import time
import json
#subprocess.call(crop, shell=True)

pygame.init()
pygame.mixer.init()

result = pygame.mixer.music.load("meme.mp3")

p = subprocess.Popen(['rhubarb -o output.json -f json-r pocketSphinx meme.wav'], cwd='/home/se101/rhubarb-lip-sync')


f = open('output.json')
  
timing = json.load(f)
  
for i in timing['mouthCues']:
    print(i)
  
f.close()

pygame.mixer.music.play()
start = time.time()
while pygame.mixer.music.get_busy():
    pass
end = time.time()
pygame.mixer.music.unload()
os.remove("output.json")