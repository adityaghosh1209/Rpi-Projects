import RPi.GPIO as GPIO
import time
import random
 
pins = (11,12,13) # R = 11, G = 12, B = 13
 
def setup():
    global pwmR, pwmG, pwmB
    GPIO.setmode(GPIO.BOARD)
    for i in pins:  # iterate on the RGB pins, initialize each and set to HIGH to turn it off (COMMON ANODE)
        GPIO.setup(i, GPIO.OUT)
        GPIO.setup(i, GPIO.HIGH)
    pwmR = GPIO.PWM(pins[0], 2000)  # set each PWM pin to 2 KHz
    pwmG = GPIO.PWM(pins[1], 2000)
    pwmB = GPIO.PWM(pins[2], 2000)
    pwmR.start(0)   # initially set to 0 duty cycle
    pwmG.start(0)
    pwmB.start(0)