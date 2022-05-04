from microbit import *
import radio
import random

def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result
key = -5

radio.on()
radio.config(channel=7)

pin = '324'                                   # <- change

while True:

    display.show(Image.SQUARE_SMALL)          # <- change
    
    message = radio.receive()
    
    if message:
        message = ascii_shift(key, message)
        pin_entered = str(message)

        if pin_entered == pin:
            radio.send("Access granted.")
            for n in range(4):
                display.show(Image.YES)
                sleep(1000)
                display.clear()
                sleep(200)
        else:
            radio.send("Access denied.")
            display.show(Image.NO)
            sleep(3000)

        display.clear()  