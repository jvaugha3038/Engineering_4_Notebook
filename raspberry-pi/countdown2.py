#type:ignore
from time import sleep
import board
import digitalio #the stuff again

red = digitalio.DigitalInOut(board.GP19)
red.direction = digitalio.Direction.OUTPUT
green = digitalio.DigitalInOut(board.GP17)
green.direction = digitalio.Direction.OUTPUT #more LED setup

green.value=False
for i in range(10,0,-1): #The Loop
    print(str(i))
    red.value=True
    sleep(.5)
    red.value=False
    sleep(.5)
print("Liftoff")
green.value=True
sleep(3) #to keep the led on for 3 seconds

