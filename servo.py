import RPi.GPIO as GPIO
import time

pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(25,50)

def drop_chip():    
    pwm.start(10)
    time.sleep(1)
    pwm.ChangeDutyCycle(5)
    time.sleep(0.15)
    pwm.ChangeDutyCycle(10)
    GPIO.cleanup()

drop_chip()
