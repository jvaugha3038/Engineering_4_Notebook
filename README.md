# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [LAUNCHPAD](#launchpad)
* [ANTI CRASH](#crash_avoidance)
* [FEA / BEAM DESIGN](#beam_design_part_1)
* [LANDING AREA](#landing_area)
* [MORSE CODE](#morse_code)
* [DATA](#data)

&nbsp;
## LAUNCHPAD

### Section Description
The first step was to use the Pico to print a 10 second countdown to the terminal, ending with "Liftoff" at 0 seconds.

### Evidence
 ![ezgif com-crop (1)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/89c188fe-a213-47d3-ba73-38d212a5781e)

### Code
[COUNTDOWN CODE](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/countdown.py)

### Reflection
The only problem I had was that I forgot how for loops worked, and then forgot how ranges worked. I tried to use a variable called "count" that I could print and decrease in the loop, but I quickly realized that that was a stupid idea and decided to do better than that. The simple solution was just "google it", so I don't really have much to say for this part. I even had to use for loops over the summer and I still forgot.

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
This assignment served the same general purpose as the last one, being the "heres how to wire a button again" assignment, with an added line of code to pull the button up or down. A metro M4 would have required extra wiring to do that, but the Pico can just do it in the code. I used a panel mount button to save space, and also because people keep ripping the pins off of the breadboard buttons somehow. Overall, not that challenging. 

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
Compared to the other ones, this one posed a slight challenge. This was mainly because I had to play The Servo Lottery since some of them just didn't work for a variety of reasons. Once I found a functioning servo, finished the code, and tested it, I was ready to record it. **However,** the servo had other plans, and then proceeded to not work ever again. In the code, I made the servo spin from 1 to 179 degrees to avoid having it get stuck at 180 again, then I got a new servo to replace the cooked one, and it worked fine.

&nbsp;

## CRASH_AVOIDANCE
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

(shows one big breadboard, but I'm really using two half-size breadboards. just the pico and the accelerometer alone take up almost an entire small breadboard.)

### Reflection
The LED part was as simple as it sounds, just "when this number is less than or equal to zero, turn the light on". The battery caused a lot of problems though, the first one being that it is **very hard** to disconnect the battery from the switch or the charger while trying not to break it. Maybe I'm just weak, but besides that, the bigger problem was that the code would work fine when connected to the computer, but when disconnected, the light would just turn on and stay on. It turned out that the ground rails on my two breadboards weren't actually connected, so once I put a jumper wire there, it worked fine. This was just an oversight on my part. The solution is to do better.

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

The OLED in fritzing doesn't have a reset pin, so I had to put it next to the other ones. Importing specific parts into fritzing is very tedious.

### Reflection
The wiring was simple enough, but the main source of problems was the screen display code. It made absolutely no sense at the start, and I had no clue whether to put it in the while loop or outside of it. Starting with a pile of lines of setup code and figuring out what order they're supposed to go in is like a puzzle. River essentially told me, "put this stuff outside of the loop and put these two lines in it" and then it just worked. Now, I sort of know what I'm doing with OLED screens. 

Side note, but I am so happy I finished all of this before we had to use whatever the hell WeVideo is. It seems way more inconvenient than ezgif ever was, even with it taking 3 minutes to upload a 10 second video.

&nbsp;

## BEAM_DESIGN_PART_1
### Assignment Description
The goal of this assignment is to design a 3D-printable beam that can support the most weight. The most notable constraints are:
-Must use/be able to attach to the provided attachment block
-Must include preset dimensions
-No overhangs
-Must be PLA, and weigh less than 13 grams.

I worked with River for this assignment, and we decided to make separate designs, then compare them and use the best one.
### Part Link 

[The Document](https://cvilleschools.onshape.com/documents/479a5d24056fdd56c88b8dd8/w/a70ad5efe5de980e63b28604/e/475bb8e7cc0dfcca94e90910?renderMode=0&uiState=651c473fcf4f7f00a8502653)

### My Base Design
![Beam Starter + Holder](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/30f978a8-55b0-448e-9ddc-f1ac7c17d05a)

### My Reasoning
I went with a triangular design mostly on a whim, but it wasn't completely silly. Triangles are strong, and I made it hollow to keep that strength while also making it as light as possible. I put tiny support beams inside of it because I figured that they *might* help, but I'm not completely sure what they'll do. Essentially, I made a big Toblerone and hoped for the best. The main issue is that the part where the weights will hang from looks like it'll just snap off.

### Post-FEA Analysis
Stress
![Assembly 1](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/9844a0d9-dc95-43e5-80a0-d95c9a904100)
Displacement
![Assembly 1 (1)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/c23b29e5-5d42-44cc-92c9-5c0091135b5d)
The stress model shows that there are two main weak spots, being the vertex where the actual beam connects to the attachment block of the beam, and the very end where the weight will hang from, as I predicted. I intend to use River's startegy of adding little walls around that part of the beam to reinforce it. For the attachment block, I plan to add a fillet to that end of the beam to spread the stress out over a greater area.
The displacement model shows exactly what you would expect; the end of the beam bends about 25cm too far, assuming it's even able to bend that far in the first place. Reinforcing the triangle itself will limit its ability to bend.

This is when it started to set in, just how long it takes for Onshape to render a simulation.
### Design Changes
I attempted to fillet the beam to the attachment block, as well as adding a wall around the part where weights will hang from. Despite my earlier predictions, neither of these made it stronger in any meaningful way (because I did it wrong), and also took a very long time to design (mainly because it takes 10 minutes to load one simulation, which will immediately unload itself if you change **anything**). Since this took forever to do only to fail, I had very little time to think of something better. I ended up settling on making the slant before the weight mount(???) a lot steeper. I ended up running out of time to check the percent improvement, but I do know it wasn't a very significant change.

### River's Base Design
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/2e1f1659-30b6-4f8c-bc48-f78be6a9ceba)

### His Reasoning
"I went with an inverted T-beam as the base shape because that design did well last year. I added lots of lightening holes down the T to stay underweight. While the loading at the end of the beam is ostensibly straight down, I knew a few beams failed in torsion last year so I added some struts to try and stiffen it in that axis. The struts are very light so they don't make much of an impact to the weight limit. One area where I know the beam could improve is in having more material near the mount point and less near the load to more efficiently handle the stress."

### The Old, Bad Designs
I won't even talk about these, I'm sure you can see why they're bad. Also, they're both over 13 grams.

![Beam Starter + Holder (1)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/b490d4cb-8e37-48d3-82ae-ec2fa41ee2bb)
![Beam Starter + Holder (3)](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/3a9b5641-829a-48b9-a65a-bb7f5ef1d2f7)

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!
&nbsp;

## LANDING_AREA
### Section Description
This first assignment was just getting 3 sets of coordinates from the user and determining the area of the triangle they formed. It also had to prompt the user to retype the coordiantes if they inputted invalid values.

### Evidence
https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/90c5bcb5-795f-47be-9377-9c4ffe9221e4

### Code
[the code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/landing1.py)

### Reflection
The split function made me sad, at least until I understood how to use it (i forgot to delete a space and also forgot to **format it correctly**). Once I got past the initial sadness I had to do the math part with variables, during which the second wave of sadness hit. Turns out I had a fundamental misunderstanding of how f-strings actually work, so I spent multiple minutes fumbling around until I solved the problem that shouldn't have existed anyways. Solution: do better.
&nbsp;

## LANDING AREA PART 2
### Section Description
On top of last assignment, this one required us to graph the triangle on an OLED screen. Sure does **sound** easy.

### Evidence
https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/84d9f5f1-5a0a-4c62-beeb-3ece45d6a942

### Code
[the code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/landing2.py)

### Reflection
Ah, OLEDs. I cannot truly explain how much of my soul was dragged away when I read the assignment title. I really, really hate using OLED screens. and now that I'm done with this assignment, I look forward to not thinking about them for at least one month. The amount of pain this caused me is incredible. Turns out the coordinates for the triangle function had to be **integers**, not **floats**, meaning the entire function took in strings, turned them into floats for the area calculation, and then turned them all into integers. I might simplify that later but for now I'm just happy to be done with this. Also, I took way longer than I feel I should have to figure out how to center the coordinates around (64,32) instead of (0,0) on the OLED. And why does the positive y-axis go down???

TLDR: Suffering. 

Also WeVideo. WeVideo is so bad. Do not use WeVideo unless you are being paid to.
&nbsp;

## MORSE_CODE
### Section Description
The first part of this assignment was to translate a user input into morse code, and print that in the terminal. It also had to quit if "-q" was typed.

### Evidence
https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/80e6e58d-4fa6-40a0-93b1-bfc29f128ee0

### Code
[moose code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/moose.py)

### Reflection
This part took me longer than I think it should have, because even though we got all of the morse code translations themselves from a dictionary, we still had to format any spaces in the prompt. I spent way too long trying things that didn't work, and then I just added a new key:value pair to the dictionary for spaces and it worked. Also, I used a function for the translation specifically because I wanted to copy over the code from landing pad 1 and just change it, instead of rewriting similar code.

(i wrote the documentation for this entire segment and then forgot to save it like a clown.)
&nbsp;

## MORSE CODE 2
### Section Description
The second part of this assignment was to make an LED blink out the morse code. wahoo

### Evidence
https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/2ffa001d-e697-4be1-b120-ebb1334c2e8a

### Code
[mouse code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/mouse.py)

### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/6a0e976f-3316-422c-8088-9ad59f2e9d6c)

### Reflection
This part was supposed to be simple, and thankfully it actually was. All of the necessary code was essentially given to us, and wiring an LED is the simplest bit of wiring we have done. It's nice to have code work as intended for once.

&nbsp;
## DATA
### Section Description
This assignment involves gathering data off of the Pico, in this case being accelerometer data. Basically, its crash avodance part 2 but we have to save that data and grab it off the Pico later.

### Evidence
https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/1ff60fe8-0b3e-4564-8028-f8bc225faeaa

https://docs.google.com/spreadsheets/d/1yZ88M6ugjBUoqh1THSC5ExokWt5CMAb1wk1IPwtQOnQ/edit#gid=0
(IMPORTANT: the data sheet lines up with my first run, not the one I recorded.)

### Code
[probably good code](https://github.com/jvaugha3038/Engineering_4_Notebook/blob/main/raspberry-pi/data1.py)

### Wiring
![image](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/a77150c5-aa87-4f2a-b096-931efdee37ed)

### Reflection
My brain was thouroughly jumbled while trying to work through this one. It started off fine, with me grabbing all of the needed code from the assignment, throwing it into the crash avoidance code, and making boot.py (i made a complete fool of myself here and i dont want to talk about it). For some reason it didnt want to actually work, which I couldn't figure out for a very long time, until I actually read my code. I forgot to replace a bit of placeholder text with the pin I was actually using. It was sad.
Long story short, that was embarassing and I don't want to talk about it.

&nbsp;
## DATA 2
### Section Description
This assignment involves turning the data from part 1 and making charts that made the data usable/readable.

### Evidence
![X, Y, and Z Acceleration of the Pico](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/a7e55318-efe5-4a8c-a64b-088aafea311d)
![Tilt Alarm](https://github.com/jvaugha3038/Engineering_4_Notebook/assets/112961338/0009321d-2d2e-4c14-9dc4-0790dcce6e4a)

### Reflection
There truly isn't much to talk about with this assignment. I've made charts and stuff with google sheets before, so it took about 5-10 minutes. Also, the radar chart is very silly looking and I tried my best to make it work and look good, but I failed.

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
