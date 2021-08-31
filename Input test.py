import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

class Inputtester:
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    
    def scence(gpiono):
        GPIO.setup(gpiono, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

        while True: # Run forever
            returnval = False
            if GPIO.input(gpiono) == GPIO.HIGH:
                returnval = True
            else:
                returnval = False
            
            return returnval
