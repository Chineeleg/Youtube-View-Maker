#!/usr/bin/env python

# This is YoutubeViewMaker 1.1
# Used for incresing the views in Youtube by @karthiksrivijay

import os

# Asking user for Video URL
URL = raw_input("Please enter the Video's URL here: ")

# Asking user for Video's Length
VideoLength = input("Please enter the Video's Length over here: ")

# Making Time Patterns

L1 = VideoLength+2
L2 = VideoLength+1
L3 = VideoLength+3
L4 = VideoLength+6
L5 = VideoLength+3
L6 = VideoLength+5
L7 = VideoLength+5
L8 = VideoLength+3
L9 = VideoLength+8
L0 = VideoLength+7

L1 = str(L1)
L2 = str(L2)
L3 = str(L3)
L4 = str(L4)
L5 = str(L5)
L6 = str(L6)
L7 = str(L7)
L8 = str(L8)
L9 = str(L9)
L0 = str(L0)

# Making Important Variables
Loops = 0

# Code Starts

while True:
    os.system("clear")
    print "Views made today are as follows:"
    print Loops
    if Loops == 0:
        os.system("timeout "+L1+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 1:
        os.system("timeout "+L2+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 2:
        os.system("timeout "+L3+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 3:
        os.system("timeout "+L4+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 4:
        os.system("timeout "+L5+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 5:
        os.system("timeout "+L6+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 6:
        os.system("timeout "+L7+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 7:
        os.system("timeout "+L8+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 8:
        os.system("timeout "+L9+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    elif Loops == 9:
        os.system("timeout "+L0+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
    else:
        os.system("timeout "+L0+" firefox "+URL+" ")
        Loops = Loops + 1
        continue
