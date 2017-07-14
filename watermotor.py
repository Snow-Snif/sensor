import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
IN1 = 20
IN2 = 21
GPIO.setmode(IN1,GPIO.OUT)
GPIO.setmode(IN2,GPIO.OUT)
PWM_freq = 200
PWM1 = GPIO.PWM(IN1,PWM_freq)
PWM2 = GPIO.PWM(IN2,PWM_freq)

PWM1.start(0)
PWM2.start(0)

while True:
    PWM1.ChangeDutyCycle(100)
    PWM2.ChangeDutyCycle(0)
    time.sleep(0.05)
GPIO.cleanup()
