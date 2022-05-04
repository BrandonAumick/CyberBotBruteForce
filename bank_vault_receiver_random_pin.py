from microbit import *
import radio
import random                                 # <- add                                 

radio.on()
radio.config(channel=7)

sleep(1000)

# pin = '011'                                 # <- comment
pin = ''                                      # <- add
for n in range(3):                            # <- add
    number = str(random.randint(0,1))         # <- add
    pin += number                             # <- add
print("Random pin =", pin)                    # <- add

while True:

    display.set_pixel(2,2,9)
    
    message = radio.receive()
    
    if message:
        if message == pin:
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