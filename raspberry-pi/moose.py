#type:ignore
from time import sleep
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}


def morse(prompt): #the Function
    if prompt == ("-q"):
        m=0
        return m
    else:
        m=("")
        prompt=upper(prompt)
        for letter in prompt:
            if letter == (" ")
                m.append(" /")
            else:
                m.append((MORSE_CODE[letter])+" ") 
        return m

while True: #the Loop
    prompt=input("Type a prompt here. Type -q to quit.   ")
    m=morse(prompt)
    sleep(1)
    if m == 0:
        print("Ending program.")
        break
    else:
        print(m) #the Output
        sleep(1)
