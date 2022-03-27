import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("../material/Video.mp4")
frames = []
nf = 5

for i in range(1000):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    frames.append(frame_gray)

    if i > nf:
        diff = cv2.absdiff(frames[i], frames[i-nf])

        #mask thresholding
        ret2, motion_mask = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)

        cv2.imshow('motion_mask',motion_mask)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(1)


# When everything done, release the capture
cap.release()