import numpy as np
import cv2


def bg_update(frame_gray,bg):
    alfa = 0.05
    bg = np.uint8(bg*(1-alfa) + alfa*frame_gray)
    #bg = frame_gray
    return bg



cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("/home/mmlab/workspace/CVLaboratories/material/Video.mp4")
background = []

for i in range(1000):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #color conversion
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)    
    
    if i == 0:
        #train background with first frame
        background = frame_gray
    else:
        #bg subtraction
        diff = cv2.absdiff(background, frame_gray)
        #mask thresholding
        ret2, motion_mask = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)
        #update background
        background = bg_update(frame_gray,background)
        # Display the resulting frame
        cv2.imshow('frame',frame)
        cv2.imshow('motion_mask',motion_mask)
        cv2.imshow('Background',background)
        cv2.waitKey(1)