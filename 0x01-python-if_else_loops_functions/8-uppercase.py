#!/usr/bin/python3
def isupper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return (True)
    else:
        return (False)

def uppercase(str):
    word = ''

    for letter in str:
        if isupper(letter) == True:
            upperletter_ascii = ord(letter)
            word = word + chr(upperletter_ascii)
        elif letter == ' ':
            word += ' ' 
        elif ord(letter) >= 97 and ord(letter) <= 122:
            upperletter_ascii = ord(letter) - 32
            word = word + chr(upperletter_ascii)
        else:
            word += letter
        
    print("{}".format(word))
