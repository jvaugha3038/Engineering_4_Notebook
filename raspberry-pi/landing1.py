#type:ignore
from time import sleep

def areaCalc(set1,set2,set3): #the Function
    try:
        S1=set1.split(",")
        S2=set2.split(",")
        S3=set3.split(",")
        x1=float(S1[0])
        y1=float(S1[1])
        x2=float(S2[0])
        y2=float(S2[1])
        x3=float(S3[0])
        y3=float(S3[1]) #splitting, then floating each set into usable numbers
        
        area=(abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))/2)) #area math
        return area
    except: #if it errors, it spits out zero and restarts
        area = 0
        return area

while True: #the Loop
    set1=input("First coordinate pair [x,y] ")
    set2=input("Second coordinate pair [x,y] ")
    set3=input("Third coordinate pair [x,y] ") #tell user to give numbers in x,y format
    area=areaCalc(set1,set2,set3)
    sleep(1)
    if area == 0:
        print("Invalid syntax. Try typing better.")
        sleep(.5)
        continue
    else:
        print(f"The area of the triangle with vertices {set1}, {set2}, {set3} is {area} square km.") #the Output
        sleep(1)
