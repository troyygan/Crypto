#!/usr/bin/python3

#Enter the encrypted message
message = 'GUVF VF ZL FRPERG ZRFFNTR'

#Same letter combination will be use

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#loop through every possible key
for key in range(len(LETTERS)):
    
    #It's important to set translated to blank string so that the previous iteration's value for translated is cleared.
    translated = ''

    #The rest is the same for ceasar cipher encryption/decryption code

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) #get the number of symbol
            num = num - key

            #handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            #add number's symbol at the end of translated 
            translated = translated + LETTERS[num]

        else:
            #just add the symbol without encrypting/decrypting
            translated = translated + symbol

    #display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))
