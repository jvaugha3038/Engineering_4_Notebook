#type:ignore
from time import sleep
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio #its even more imports

displayio.release_displays()

import busio
import board
from digitalio import DigitalInOut, Direction, Pull #the stuff again
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle   #importing the ability to Shape

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
# create the display group
splash = displayio.Group()
circle = Circle(64, 32, 2, outline=0xFFFF00) #origin
splash.append(circle)
hline = Line(64,0,64,64, color=0xFFFF00) #x-axis
splash.append(hline)
vline = Line(0,32,128,32, color=0xFFFF00) #y-axis
splash.append(vline)
display.show(splash) #showing all of that stuff
def areaCalc(set1,set2,set3):
    try:
        S1=set1.split(",")
        S2=set2.split(",")
        S3=set3.split(",") #splitting all the stuff

        x1=float(S1[0])
        y1=float(S1[1])
        x2=float(S2[0])
        y2=float(S2[1])
        x3=float(S3[0])
        y3=float(S3[1]) #floating all the stuff
        area=(abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2))
        tx1=int(64+x1)
        ty1=int(32-y1)
        tx2=int(64+x2)
        ty2=int(32-y2)
        tx3=int(64+x3)
        ty3=int(32-y3) #int-ing all the stuff
        triangle = Triangle(tx1, ty1, tx2, ty2, tx3, ty3, outline=0xFFFF00) #triangle
        splash.append(triangle)
        display.show(splash) #showing the triangle
        return area
    except:
        area = 0
        return area #if it broke, the area is now zero

while True:
    set1=input("First coordinate pair [x,y] ")
    set2=input("Second coordinate pair [x,y] ")
    set3=input("Third coordinate pair [x,y] ") #user inputs
    area=areaCalc(set1,set2,set3)
    if area == 0:
        print("Invalid syntax. Try typing better.") #tells the user to do better
        sleep(.5)
        continue
    else:
        print(f"The area of the triangle with vertices [{set1}], [{set2}], [{set3}] is {area} square km.")
        sleep(2)
