from microbit import *
import radio
import random

''' Function converts plaintext to ciphertext using key '''

def scramble(word, encrypt):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){};:/?.>,<qwertyuiopasdfghjklzxcvbnm`~=+"
    crypta = "MF>V@Jrm~EteLU`?B*YaT:hvn.Q/WRC,N%zH^xqOS<#lDZku;I}{diPscG&+o$pX=AgywKfb)!j("
    result = ''
    if encrypt is False:
        temp = alpha
        alpha = crypta
        crypta = temp

    for letter in word:
        index = alpha.find(letter)
        result = result + crypta[index]

    return result
    
    
    

''' Script starts from here... '''

radio.on()
radio.config(channel=3)

sleep(1000)

string_list = ["HAPPY", "SAD", "ANGRY"]

while True:
    
    for packet in string_list:
        print("packet:", packet)
        display.show(getattr(Image, packet))
        packet = scramble(packet, True)
        print("Send encrypted:", packet)
        radio.send(packet)
        sleep(2500)