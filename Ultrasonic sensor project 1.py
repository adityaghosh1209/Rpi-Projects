import Ultrasonic_sensor
import RGB_Led
import time
import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(11, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
GPIO.setup(13, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
GPIO.setup(15, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT

US = Ultrasonic_sensor.Run
Led = RGB_Led.Run
#"------------------------------------- LED Code
redPin = 11   #Set to appropriate GPIO
greenPin = 13 #Should be set in the 
bluePin = 15  #GPIO.BOARD format


def setup(R, G, B):
    redPin = R   #Set to appropriate GPIO
    greenPin = G #Should be set in the 
    bluePin = B  #GPIO.BOARD format

def blink(pin):
    #GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def redOn():
    blink(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)
#---------------------------------------end LED code


while True:
    dist = US.distance(12, 18)
    print ("Measured Distance = %.1f cm" % dist)
    time.sleep(1)
    if (dist>=100.0):
        print("Tank empty")
        greenOn()
        magentaOff()
        
    elif (dist >= 50.0):
        print("tank 50% filled WARNING")
        yellowOn()
        blueOff()
        

    elif (dist >=10.0):
        print( "Tank fully filled")
        redOn()
        cyanOff()
        #GPIO.output(11, False)  ## Turn on Led
       # GPIO.output(13, True)
        #GPIO.output(15, False)
    else:
        print( "error detecting level")
    