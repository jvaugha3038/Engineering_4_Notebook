#type:ignore

import adafruit_mpu6050
import busio
import time
import board
from digitalio import DigitalInOut, Direction #the stuff again

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
red = DigitalInOut(board.GP16)
red.direction = Direction.OUTPUT

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c) #the setup soup

with open("/data.csv", "a") as datalog: #the thing that allows the data the data to be Grabbed
    while True: #the Loop
        acc = mpu.acceleration
        print("X = ["+str(acc[0])+"]| Y = ["+str(acc[1])+"]| Z = ["+str(acc[2])+"]") #prints acceleration values using the archaic str() method
        if acc[2] <= 0:
            red.value = True #if number small light go
            tilt=1
        else:
            red.value = False #if number big light no
            tilt=0 
        t=time.monotonic()
        datalog.write(f"{t},{acc[0]},{acc[1]},{acc[2]},{tilt}\n")
        led.value = True
        time.sleep(0.25) #wait
        datalog.flush()
        led.value = False 