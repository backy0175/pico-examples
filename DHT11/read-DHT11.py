"""This is simple example to read temperature and humidity"""

from machine import Pin
from time import sleep
import dht
    
# prepare to read DHT11/DHT22
sensor = dht.DHT11(Pin(2, Pin.IN, Pin.PULL_UP)) 
#sensor = dht.DHT22(Pin(2, Pin.IN, Pin.PULL_UP)) 
 
while True:
    # get temperature and humidity
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
     
    print("Temperature: {:.1f}°C   Humidity: {:.1f}%".format(temp, hum))
    sleep(10)
