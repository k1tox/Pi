#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

#Setup

#Outputs - Pins 13, 16 and 19
GPIO.setup(13,GPIO.OUT) # Pin 13 -> Sim 1
GPIO.setup(16,GPIO.OUT) # Pin 16 -> Posso ultrapassar 2
GPIO.setup(19,GPIO.OUT) # Pin 19 -> Nao 1

#Inputs - Pins 20, 21 and 26
GPIO.setup(20,GPIO.IN) # Pin 20 ->  Sim 2
GPIO.setup(21,GPIO.IN) # Pin 21 ->  Nao 2
GPIO.setup(26,GPIO.IN) # Pin 26 ->  Posso ultrapassar 1

GPIO.setup(10,GPIO.IN) # Pin 10 -> User interface


# Functions

def BeTaked():
    #Code if the car behind me wants to takeover

    GPIO.output(16,GPIO.HIGH) # Ask to front sensor if it safe
    nao = 0
    sim = 0
    while ((sim == 0) & (nao == 0)):
        # wait here
        nao = GPIO.input(21)
        sim = GPIO.input(20)

    if(sim == 1):
        GPIO.output(13,GPIO.HIGH) # Send yes signal to back sensor
    elif(nao == 1):
        GPIO.output(19,GPIO.HIGH) # Send no signal to back sensor
    else:
        pass

    return;

def Take():
    # Code if I want to takeover

    GPIO.output(16,GPIO.HIGH) # Ask to front sensor if it safe
    nao = 0
    sim = 0
    while ((sim == 0) & (nao == 0)):
        # wait here
        nao = GPIO.input(21)
        sim = GPIO.input(20)

    if(sim == 1):
        pass # call function to takeover - (delete pass)
    elif(nao == 1):
        pass # do nothing?
    else:
        pass

    return;

# Body
while 1:
    CanBehind_flag = GPIO.input(26)
    CanI_flag = GPIO.input(10)

    if(CanBehind_flag == 1):
        BeTaked()

    if(CanI_flag == 1):
        Take()
    time.sleep(1)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
