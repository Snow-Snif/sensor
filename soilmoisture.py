import spidev
import time
import os


spi = spidev.SpiDev()
spi.open(0, 0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1]&3) << 8) + adc[2]

def convertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

moisture2_pin = 2

delay = 1

while True:
    data = ReadChannel(2)
    volts = convertVolts(data, 5)
    print "--------------------------------------------"
    print("Moisture (Ground): {} ({}V)".format(data, volts))
    time.sleep(delay)

