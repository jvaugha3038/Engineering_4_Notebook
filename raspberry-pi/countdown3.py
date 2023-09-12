#type:ignore
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull #the stuff again

red = DigitalInOut(board.GP19)
red.direction = Direction.OUTPUT
green = DigitalInOut(board.GP17)
green.direction = Direction.OUTPUT #more LED setup
green.value=False
button = DigitalInOut(board.GP15)
button.direction = Direction.INPUT
button.pull = Pull.DOWN #button setup

while button.value == False:
    pass

for i in range(10,0,-1): #The Loop
    print(str(i))
    red.value=True
    sleep(.5)
    red.value=False
    sleep(.5)
    if button.value==True: #ends countdown when pressed
        print("NO MORE")
        break
else:
    print("Liftoff")
    green.value=True
    sleep(3) #to keep the led on for 3 seconds

