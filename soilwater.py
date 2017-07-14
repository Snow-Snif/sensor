import spidev
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
spi = spidev.SpiDev()
spi.open(0, 0)

IN1 = 20
IN2 = 21
GPIO.setmode(IN1,GPIO.OUT)
GPIO.setmode(IN2,GPIO.OUT)
PWM_freq = 200
PWM1 = GPIO.PWM(IN1,PWM_freq)
PWM2 = GPIO.PWM(IN2,PWM_freq)
PWM1.start(0)
PWM2.start(0)

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
    if(data <= 300):
        print("Dry")
        PWM1.ChangeDutyCycle(100)
        PWM2.ChangeDutyCycle(0)
        time.sleep(0.05)
    elif(301 < data and data < 699):
        print("Normal")
        PWM1.ChangeDutyCycle(0)
        PWM2.ChangeDutyCycle(0)
        time.sleep(0.05)
    else:
        print("Wet")
        PWM1.ChangeDutyCycle(0)
        PWM2.ChangeDutyCycle(0)
        time.sleep(0.05)

    time.sleep(delay)
GPIO.cleanup()

