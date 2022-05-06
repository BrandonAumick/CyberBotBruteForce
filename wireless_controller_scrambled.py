from microbit import *
import radio



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

print("\nSpeeds are -100 to 100\n")

while True:
    try:
        vL = int(input("Enter left speed: "))
        vR = int(input("Enter right speed: "))
        ms = int(input("Enter ms to run: "))

        dictionary = {  }
        dictionary['vL'] = vL
        dictionary['vR'] = vR
        dictionary['ms'] = ms

        packet = str(dictionary)
    
        print("Send: ", packet)
        packet = scramble(packet, True)
        print("Encrypted: ", packet)
        radio.send(packet)
    
        print()

    except:
        print("Error in value entered.")
        print("Please try again. \n")
        