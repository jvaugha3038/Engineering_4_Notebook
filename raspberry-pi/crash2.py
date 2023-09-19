#type:ignore

import adafruit_mpu6050
import busio
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull #the stuff again
import pwmio

red = DigitalInOut(board.GP16)
red.direction = Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c) #the setup soup

while True: #the Loop
    acc = mpu.acceleration
    print("X = ["+str(acc[0])+"]| Y = ["+str(acc[1])+"]| Z = ["+str(acc[2])+"]") #prints acceleration values using the archaic str() method
    if acc[2] <= 0:
        red.value = True #if number small light go
    else:
        red.value = False #if number big light no
    sleep(0.1) #wait