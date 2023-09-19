# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LAUNCHPAD](#LAUNCHPAD_PART_1)
* [ANTI-CRASH](#CRASH_AVOIDANCE_PART_1)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## LAUNCHPAD PART 1
### Section Description
The first step was to use the Pico to print a 10 second countdown to the terminal, ending with "Liftoff" at 0 seconds.

### Evidence
 ![ezgif com-crop (1)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/89c188fe-a213-47d3-ba73-38d212a5781e)

### Code
[COUNTDOWN CODE](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/countdown.py)

### Reflection
The only problem I had was that I forgot how for loops worked, and then forgot how ranges worked. The simple solution was just "google it", so I don't really have much to say for this part.

&nbsp;
## LAUNCHPAD PART 2
### Section Description
The second step was to make a red LED blink on every second of the countdown, then turn on a green LED on liftoff.

### Evidence 
![ezgif com-optimize](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/310a8bee-1ce3-48b6-b89f-3227f89c8cbe)

### Wiring
shoutout to fritzing for being better than tinkercad could ever be
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/d4423bf0-2795-4a47-a422-45aa676d5291)

![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/aee50b42-04c4-4c0e-88f9-4d5604a848b0)
Also I will be using this image forever so I'm putting it here.
### Code
[The Code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/countdown2.py)

### Reflection
This assignment was the mandatory "you forgot how LED wiring works and thus the assignment takes 3x longer" assignment this year. Once I remembered what I was doing (and which side of the LED is positive, its the long side) it ended up being very easy.

&nbsp;
## LAUNCHPAD PART 3
### Section Description
Adding onto the previous parts, the next step was to add a button to start the countdown, and pressing the button again would force stop the countdown.

### Evidence 
![ezgif com-optimize (1)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/1d1aeb7e-c5d0-4cfd-a510-139ebae6127a)
 
### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/cf47942b-8954-4543-b3cb-bc139399524a)

### Code
[the code :)](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/countdown3.py)

### Reflection

This assignment served the same general purpose as the last one, being the "heres how to wire a button again" assignment. I used a panel mount button to save space. Overall, not that challenging.

&nbsp;
## LAUNCHPAD PART 4
### Section Description
The final part of this assignment was to make a servo spin from 0 to 180 degrees on liftoff.

### Evidence 
![ezgif com-optimize (2)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/27660665-013f-4f44-a141-0bbd319a9b01)

### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/d6ad9118-9459-41f9-af57-cbfa19f47390)

### Code
[the whole everything](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/countdown4.py)

### Reflection
Compared to the other ones, this one posed a slight challenge. This was mainly because I had to play The Servo Lottery since some of them just didn't work for a variety of reasons. Once I found a functioning servo, finished the code, and tested it, I was ready to record it. **However,** the servo had other plans, and then proceeded to not work ever again. In the code, I made the servo spin from 1 to 179 degrees to avoid having it get stuck at 180 again, then I got a new servo and it worked fine.

&nbsp;

## CRASH AVOIDANCE PART 1
### Section Description
The goal of the first step was to get an accelerometer to print out values to the serial monitor.

### Evidence
![ezgif com-crop (2)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/e8f522e7-8a56-4349-a41b-aed342515015)

### Code
[very good programming](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/crash1.py)

### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/d8c58841-c568-4d11-994e-f8629d0b234e)

### Reflection
This first step was VERY easy. My final project in engineering 3 used a gyroscope, which is wired and coded in essentially the same way since they're the same device. That means that I was able to just check my old documentation and wiring to see what to do.

&nbsp;

## CRASH AVOIDANCE PART 2
### Section Description
The goal of the second step was to get a battery to power the pico, as well as adding a warning light when the system was tilted 90+ degrees.

### Evidence
![ezgif com-crop (3)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/7e0781bb-3267-4c13-bcdf-c239e512b1dc)

### Code
[even better code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/crash2.py)

### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/c9af72a1-f693-4ef2-9eda-9ca59792c126)
(shows one big breadboard, but I'm really using two half-size breadboards.)
### Reflection
The LED part was as simple as it sounds, just "when this number is less than or equal to zero, turn the light on". The battery caused a lot of problems though, the first one being that it is **very hard** to disconnect the battery from the switch or the charger while trying not to break it. Maybe I'm just weak, but besides that, the bigger problem was that the code would work fine when connected to the computer, but when disconnected, the light would just turn on and stay on. It turned out that the ground rails on my two breadboards weren't actually connected, so once I put a jumper wire there, it worked fine. This was just an oversight on my part.

&nbsp;

## CRASH AVOIDANCE PART 3
### Section Description
The goal of the third step was to get an OLED screen to display gyroscope values, still adding onto the first two parts.

### Evidence
![ezgif com-optimize (3)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/52e9eee7-9341-4b6c-8ef1-72b08aa5cab9)

### Code
[code...?](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/crash3.py)

### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/8e6834d9-dec7-40b0-8687-b108b0b753ea)
The OLED in fritzing doesn't have a reset pin, so I had to put it next to the other ones.

### Reflection
The wiring was simple enough, but the main source of problems was the screen display code. It made absolutely no sense at the start, and I had no clue whether to put it in the while loop or outside of it. River essentially told me, "put this stuff outside of the loop and put these two lines in it" and then it just worked. Now, I sort of know what I'm doing with OLED screens.

&nbsp;

## TEMPLATE (plz copy)
### Section Description
what was the assignment

### Evidence
gif/video of the thing doing what its meant to do

### Code
[some funny link name](the link)

### Wiring
fritzing saves lives

### Reflection
what took forever, what was easy, was it miserable and why

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[test link lmao](raspberry-pi/temp.py)
### Test Image
![ferret](images/0.png)  
### Test GIF
![kirby!!!](images/kirby-headphones.gif)  
