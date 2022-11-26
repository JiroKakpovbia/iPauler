import pygame
import os
import subprocess
import time
import json

pygame.init()
pygame.mixer.init()

result = pygame.mixer.music.load("meme.mp3")
subprocess.run(["Rhubarb-Lip-Sync-1.13.0-Linux/rhubarb -o output.json -f --json-r --pocketSphinx meme.mp3"])


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