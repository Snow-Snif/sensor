import spidev
import time
import os
import RPi.GPIO as GPIO
import dht11
import datetime

spi = spidev.SpiDev()
spi.open(0, 0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin=4)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1]&3) << 8) + adc[2]

def convertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

light_channel = 1

while True:
    light_level = ReadChannel(1)
    light_volts = convertVolts(light_level, 2)

    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        print("Light: {} ({}V)".format(light_level, light_volts))
        print "--------------------------------------------"

    time.sleep(5)

