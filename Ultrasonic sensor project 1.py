import Ultrasonic_sensor
import RGB_Led
import time

US = Ultrasonic_sensor.Run
Led = RGB_Led.Run

#US.setup(18, 24)
Led.setup(11, 15, 13)

Led.blink(11)

while True:
    dist = US.distance(18, 24)
    print ("Measured Distance = %.1f cm" % dist)
    time.sleep(1)
    if (dist>=100.0):
        print("Tank empty")
    elif (dist >= 50.0):
        print("tank 50% filled WARNING")
    elif (dist >=10.0):
        print( "Tank fully filled")
    else:
        print( "error detecting level")
    