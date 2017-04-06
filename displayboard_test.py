#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime

lcd = Adafruit_CharLCD()

lcd.begin(16, 1)

while 1:
    lcd.clear()
    lcd.message('Hello, world!\n')
    lcd.message('Hola, mundo!\n')
    sleep(2)
