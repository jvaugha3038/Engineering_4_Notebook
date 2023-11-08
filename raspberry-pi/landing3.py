#type:ignore
from time import sleep
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio #its even more imports
from math import sqrt

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
set0=[[-50,-17,-57,12,-22,-7],[28,-14,60,-7,54,18],[45,30,51,-1,18,6],[5,5,19,15,22,10]]
area=0
dist=0
def areaCalc(set0):
    try:
        sets=set0.split(",",3)
        S=0
        t1=coordFind(sets[S])
        S=1
        t2=coordFind(sets[S])
        S=2
        t3=coordFind(sets[S])
        S=3
        t4=coordFind(sets[S])
        if t1[1] < t2[1] and t1[1] < t3[1] and t1[1] < t4[1]:
            x=[sets[0[0,1]]]
            y=[sets[0[2,3]]]
            z=[sets[0[4,5]]]
        if t2[1] < t1[1] and t2[1] < t3[1] and t2[1] < t4[1]:
            x=[sets[1[0,1]]]
            y=[sets[1[2,3]]]
            z=[sets[1[4,5]]]
        if t3[1] < t2[1] and t3[1] < t2[1] and t3[1] < t4[1]:
            x=[sets[2[0,1]]]
            y=[sets[2[2,3]]]
            z=[sets[2[4,5]]]
        if t4[1] < t2[1] and t4[1] < t3[1] and t4[1] < t3[1]:
            x=[sets[3[0,1]]]
            y=[sets[3[2,3]]]
            z=[sets[3[4,5]]]
        return x,y,z,area,dist
    except:
        return area, dist #if it broke, the area is now zero

def coordFind(sets[S]):
    x1=float(S[0])
    y1=float(S[1])
    x2=float(S[2])
    y2=float(S[3])
    x3=float(S[4])
    y3=float(S[5]) #floating all the stuff
    area = (abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2))
    Cx = (abs((x1 + x2 + x3)/3))
    Cy = (abs((y1 + y2 + y3)/3))
    dist = sqrt(((Cx-0)**2)+((Cy-0)**2))
    tx1=int(64+x1)
    ty1=int(32-y1)
    tx2=int(64+x2)
    ty2=int(32-y2)
    tx3=int(64+x3)
    ty3=int(32-y3) #int-ing all the stuff
    triangle = Triangle(tx1, ty1, tx2, ty2, tx3, ty3, outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)
    return area, dist

while True:
    area=areaCalc(set0)
    if area == 0:
        print("Something broke.") #tells me to code better
        sleep(.5)
        continue
    if dist == 0:
        print("Something else broke.") #tells me to code better
        sleep(.5)
        continue
    else:
        print(f"The closest suitable landing area has vertices ({x}, {y}, {z}). The area is {area} km2 and the centroid is {dist} km away from base.")
        sleep(2)