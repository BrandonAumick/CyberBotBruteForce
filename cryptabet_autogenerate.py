from microbit import *
import random

sleep(1000)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
size = len(alpha)

print("size: ", size)
print("alpha:", alpha)

sleep(1500)

crypta = ""

n = 0
while n < size:
    sleep(50)
    r = random.randint(0, size-1)
    c = alpha[r]
    print("r:", r, ", c:", c)
    if crypta.find(c) == -1:
        crypta = crypta + c
        n = n + 1
        print("n:", n, ", crypta:", crypta)

sleep(1000)    
print("crypta:", crypta)
sleep(100)
print()