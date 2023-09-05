from time import sleep
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
while True:
    led.value = True
    sleep(1)
    led.value = False
    sleep(1)


