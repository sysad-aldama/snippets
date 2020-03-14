# Goal: To access your webcams via opencv-python 
# Requirements: pip install opencv-python numpy
# Note: I highly recommend installing anaconda for python 3.x 
# Anaconda installer: https://www.anaconda.com/distribution/
# Written by: JP Aldama [Quaxis Corporation for Research & Innovation]
import os
import cv2
import numpy as np

# Messages indicating the state of the program
# Sometimes python may take long and you want to know which code is processing
# TODO turn this into a function that returns current message
MESSAGES = [
    '[cv2_webcam info] Program started... ',                           # MESSAGES[0]
    '[cv2_webcam info] Webcam initializing...',                        # MESSAGES[1]       
    '[cv2_webcam info] Webcam loaded!',                                # MESSAGES[2]
    '[cv2_webcam info] Press q to exit program',                       # MESSAGES[3]
    '[cv2_webcam info] Program exiting...',                            # MESSAGES[-3]
    '[cv2_webcam info] ERROR: webcam unavailable. Program exiting...', # MESSAGes[-2]
    '[cv2_webcam info] ERROR: Frame not received. Program exiting...', # MESSAGES[-1]
]

current_message = MESSAGES[0]
print(current_message)

current_message = MESSAGES[1]
print(current_message)

# Init webcam NOTE: if you have multiple webcams, 0 is always your integrated webcam
# If you have multiple then 1 is your external webcam, 2,3 etc...
capture = cv2.VideoCapture(0)

current_message = MESSAGES[2]
print(current_message)

"""
To load a video just run the next line and comment the previous line.
source = cv2.VideoCapture('test.mp4')
"""

# Check if webcam is initialized. If isOpened() returns False, program closes.
if not capture.isOpened():
    current_message = MESSAGES[-2]
    print(current_message)
    exit()
else: 
    current_message = 'Program Running...'    
    print(current_message)

# Main loop
while capture.isOpened():
    
    current_message = MESSAGES[3]
    # Capture each frame
    ret, frame = capture.read()
    
    # If frame is read properly ret is True
    if not ret:
        current_message = MESSAGES[-1]
        print(current_message)
        break

    # ---MAIN PROGRAM OPERATION---# 
    
    # Convert frame to grayscale
    # If color, delete next line, and on ln 70 change grayscale to frame
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Title display window and show grayscale frame 
    cv2.imshow('cv2_webcam example', grayscale)
    
    # Wait for key 'q' to terminate main loop
    if cv2.waitKey(1) & 0xFF == 27:
        break
        current_message = MESSAGES[-2]
        print(current_message)
    else: 
        continue    
       
# Release capture and close all displays
capture.release()
cv2.destroyAllWindows()

