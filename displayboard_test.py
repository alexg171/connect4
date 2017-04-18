#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime

lcd = Adafruit_CharLCD()

lcd.begin(16, 1)

message_top = 'default'
message_btm = 'default'

def lcd_message(msg_t, msg_b):
    global message_top
    global message_bottom
    message_top = msg_t
    message_btm = msg_b

while 1:
    lcd.clear()
    lcd.message(message_top)
    lcd.message(message_btm)
    sleep(2)
