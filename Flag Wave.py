#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm = GPIO.PWM(11, 50)

press = input("Press a key to start, Ctrl+C to finish\n")
print("Flag waving in progress...")

try:
    while True:
        pwm.start(1)
        sleep(1)
        
        pwm.start(5)
        sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nFlag waving session ended. :(")
