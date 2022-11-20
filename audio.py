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
                
p.play()
