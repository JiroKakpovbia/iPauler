from subprocess import call
import speech_recognition as sr
import serial
import RPi.GPIO as GPIO    

def speech_to_text():
    with sr.Microphone() as mic:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(mic)
        print("Listening...");
        audio = recognizer.listen(source)
        print("got it");
    return audio

def voice(audio1):
       try:
         recognizer = sr.Recognizer()
         text1 = recognizer.recognize_google(audio1)
##         call('espeak '+text, shell=True)
         print ("you said: " + text1);
         return text1;
       except sr.UnknownValueError:
          call(["espeak", "-s140  -ven+18 -z" , "Google Speech Recognition could not understand"])
          print("Google Speech Recognition could not understand")
          return 0
       except sr.RequestError as e:
          print("Could not request results from Google")
          return 0

def main(text):
       audio1 = speech_to_text()
       text = voice(audio1);
       text = {}