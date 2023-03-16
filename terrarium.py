#!/usr/bin/python
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

TRIG = 18
ECHO = 24

PUMP_RELAY = 23

DHT_DATA = 4
DHT_TYPE = 11

class Terrarium:
  def __init__(self):
    self.last_misted = 0
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.setup(PUMP_RELAY, GPIO.HIGH)
    GPIO.output(TRIG, False)
    time.sleep(2) # waiting for sensor to settle

  def get_water_level(self): # in centimeters
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_stop = time.time()

    pulse_time = pulse_stop - pulse_start # speed of pulse traveling to the water surface and back 
    distance = (pulse_time/2) * 34300 # speed of sound (34300 cm/s) = distance/time
    
    return 28 - distance

  def get_humidity(self):
    humidity = Adafruit_DHT.read_retry(DHT_TYPE, DHT_DATA)[0]
    return humidity

  def get_temp(self):
    temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_DATA)[1]
    return temperature

  def get_data(self):
    return Adafruit_DHT.read_retry(DHT_TYPE, DHT_DATA)
  
  def get_time_last_misted(self):
    return self.last_misted

  def mist(self, num_seconds):
    water_level = self.get_water_level()
    if(water_level < 5): #cm
      raise Exception("Water level low", water_level)
    if((time.time() - self.last_misted) < 30):
      raise Exception("Wait to mist")
    GPIO.setup(PUMP_RELAY, GPIO.LOW) # pump on
    time.sleep(num_seconds)
    GPIO.setup(PUMP_RELAY, GPIO.HIGH) # pump off
    self.last_misted = time.time()