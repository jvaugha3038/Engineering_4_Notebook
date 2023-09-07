from time import sleep
import board
import digitalio #all the imports

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT #led setup
count=10

for i in range(10,0,-1): #repeats 10 times
    print(str(i))
    sleep(1)
print("Liftoff")

