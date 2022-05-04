from microbit import *
import radio

def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result
key = 5

radio.on()
radio.config(channel=7)

pin = ''
n = 0

while True:

    x = len(pin)
    
    if button_a.was_pressed():
        if n < 5:
            n += 1
            if n is not 0:
                y = n - 1
                display.set_pixel(x, y, 9)
        else:
            for y in range(0, 5):
                display.set_pixel(x, y, 0)
            n = 0
    if button_b.was_pressed():
        pin += str(n)
        n = 0
        if len(pin) == 3:
            pin = ascii_shift(key, pin)
            radio.send(pin)
            display.scroll(pin)
            pin = ''
            display.clear()