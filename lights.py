import RPi.GPIO as GPIO
from time import sleep
import numpy as np

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)  
#set red,green and blue pins
redPin = 11
greenPin = 13
bluePin = 15
#set pins as outputs
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)



def turnOff():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def white():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
    
def red():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.LOW)
def green():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.LOW)
def blue():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
def purple():
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
def yellow():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def disco():

    a = 0
    b = 0
    c = 0
    while True:
        while a == b and b == c and c ==2:
            a = np.random.choice((1,2))
            b = np.random.choice((1,2))
            c = np.random.choice((1,2))

        if a == 1:
            GPIO.output(greenPin,GPIO.HIGH)
        else:
            GPIO.output(greenPin,GPIO.LOW)
        if b == 1:
            GPIO.output(redPin,GPIO.HIGH)
        else:
            GPIO.output(redPin,GPIO.LOW)
        if c == 1:
            GPIO.output(bluePin,GPIO.HIGH)
        else:
            GPIO.output(bluePin,GPIO.LOW)

        sleep(0.5)







if __name__ == "__main__":
    run = True

    while run:

        val = input("choose color: ")
        if(val == "0"):
            turnOff()
        if(val == "1"):
            red()
        if(val == "2"):
            green()
        if(val == "3"):
            blue()
        if(val == "4"):
            white()