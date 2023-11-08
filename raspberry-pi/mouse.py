#type:ignore
from time import sleep
import board
from digitalio import DigitalInOut, Direction

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
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

red = DigitalInOut(board.GP16)
red.direction = Direction.OUTPUT
def morse(prompt): #the Function
    if prompt == ("-q"):
        m=("")
        return m
    else:
        m=("")
        prompt=prompt.upper()
        for letter in prompt:
            m = f"{m} {MORSE_CODE[letter]}"
        return m

while True: #the Loop
    prompt=input("Type a prompt here. Type -q to quit.   ")
    m=morse(prompt)
    sleep(1)
    if m == "":
        print("Ending program.")
        break
    else:
        print(m) #the Output
        for letter in m:
            if letter == ".":
                red.value=True
                sleep(dot_time)
            if letter == "-":
                red.value=True
                sleep(dash_time)
            if letter == " ":
                red.value=False
                sleep(between_letters)
            if letter == "/":
                red.value=False
                sleep(between_words)
            red.value=False
            sleep(between_taps)