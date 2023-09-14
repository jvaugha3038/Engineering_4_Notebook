#type:ignore

import adafruit_mpu6050
import busio
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull #the stuff again
import pwmio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Acceleration = "+str(mpu.acceleration))
    sleep(0.1)