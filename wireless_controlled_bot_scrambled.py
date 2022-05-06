from cyberbot import *
import radio

print('test')

def scramble(word, encrypt):
    alpha = "vLR{}:,'01234 56789ms"
    crypta = "v9L:3405'R286, 7{}1sm"   
    result = ''
    if encrypt is False:
        temp = alpha
        alpha = crypta
        crypta = temp

    for letter in word:
        index = alpha.find(letter)
        result = result + crypta[index]

    return result


radio.on()
radio.config(channel=3,length=64)

sleep(1000)

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        print("Receive: ", packet)
        packet = scramble(packet, False)
        print("Decrypted: ", packet)
        
        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)