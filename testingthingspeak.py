import Adafruit_DHT
from time import time, sleep
from urllib.request import urlopen
import sys

WRITE_API = "Y82H1TUDTF2LPTMD" # Replace your ThingSpeak API key here
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(WRITE_API)

SENSOR_PIN = 4
SENSOR_TYPE = Adafruit_DHT.DHT11

SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds

try:
    while True:
        
        if (time() - SensorPrevSec) > SensorInterval:
            SensorPrevSec = time()
            print("inv" + str(time() - SensorPrevSec) + " " +str(SensorInterval))
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
            print("Humidity = {:.2f}%\tTemperature = {:.2f}C".format(humidity, temperature))
        
        if (time() - ThingSpeakPrevSec) > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}".format(temperature, humidity)
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print("Response: {}".format(conn.read()))
            conn.close()
            
            sleep(15)
		#try:
			#humidity, temperature = Adafruit_DHT.read_retry(SENSOR_TYPE, SENSOR_PIN)
			#print("Humidity = {:.2f}%\tTemperature = {:.2f}C".format(humidity, temperature)) 
		#except:
			#pass   

		#thingspeakHttp = BASE_URL + "&field1={:.2f}&field2={:.2f}".format(temperature, humidity)
		#print(thingspeakHttp)
			
		#conn = urlopen(thingspeakHttp)
		#print("Response: {}".format(conn.read()))
		#conn.close()

		#sleep(15)
            
except KeyboardInterrupt:
    conn.close()
