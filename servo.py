import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 100)
p.start(5)
p.ChangeDutyCycle(100)
GPIO.cleanup()
