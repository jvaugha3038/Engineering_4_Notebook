#type:ignore
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio #its even more imports

displayio.release_displays()


import adafruit_mpu6050
import busio
from time import sleep
import board
from digitalio import DigitalInOut, Direction, Pull #the stuff again
import pwmio
#mpu is 0x68
#OLED is 0x3d
red = DigitalInOut(board.GP16)
red.direction = Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #address is more specific now

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
# create the display group
splash = displayio.Group()
# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

while True:
    acc = mpu.acceleration
    gyro = mpu.gyro #variables to make my life easier
    print("X = ["+str(acc[0])+"]| Y = ["+str(acc[1])+"]| Z = ["+str(acc[2])+"]") #prints the acceleration values
    if acc[2] <= 0:
        red.value = True
    else:
        red.value = False

    text_area.text = f"X = {gyro[0]:.2f} rad/s\nY = {gyro[1]:.2f}rad/s\nZ = {gyro[2]:.2f} rad/s" #text that updates every loop
    # send display group to screen
    display.show(splash)

    sleep(0.1) #wait