#type:ignore

from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull #the stuff again
import pwmio
from adafruit_motor import servo #NEW servo setup!! so exciting

pwm_servo = pwmio.PWMOut(board.GP12, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500) #more setup

red = DigitalInOut(board.GP19)
red.direction = Direction.OUTPUT
green = DigitalInOut(board.GP17)
green.direction = Direction.OUTPUT #more LED setup
green.value=False
button = DigitalInOut(board.GP15)
button.direction = Direction.INPUT
button.pull = Pull.DOWN #button setup
servo1.angle = 1 #setting angle to 1 bc 0 sometimes gets the servo stuck

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
    servo1.angle = 179 #set to 179 instead of 180 for same reason
    green.value=True
    sleep(3) #to keep the led on for 3 seconds
