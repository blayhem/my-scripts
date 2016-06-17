# Script in Python to power off the RPi connecting two GPIO pins
import RPi.GPIO as GPIO
from time import sleep
from os import system

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)

while True:
  if GPIO.input(22):
    system('sudo poweroff')
  sleep(0.1)

