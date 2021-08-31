#----this is only applicable for DTH 11-----------HumiditySensor--------------------------
#note: insert the data pin of the DTH sensor to GPIO pin 4 in the PI
#     Aditya Ghosh
import time
import Adafruit_DHT

class SensorReadings:
    #physical Variables
    DHT_SENSOR = Adafruit_DHT.DHT11

    def Read(self, DHT_PIN):
        DHT_SENSOR = Adafruit_DHT.DHT11
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        DTH = []        
        if humidity is not None and temperature is not None:
            time.sleep(3)
            #print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
            DTH.append(temperature)
            DTH.append(humidity)
        else:
            temperature = "sensing..."
            humidity = "sensing..."
            #print("Sensor failure. Check wiring.");
            DTH.append(temperature)
            DTH.append(humidity)
        
        return DTH

        