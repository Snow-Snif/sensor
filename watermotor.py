import RPi.GPIO as GPIO
import time
import sys

pwn_pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setmode(16,GPIO.OUT)

pwm_led = GPIO.PWM(pwn_pin,500)
pwm_led.stat(100)

try:
    while True:
        duty = 80
        pwm_led.ChangeDutyCycle(duty)
except KeyboardInterrupt:
    print("stop")
    sys.exit(0)


