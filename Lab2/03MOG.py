import numpy as np
import cv2

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("../material/Video.mp4")

learningRate = -1
history = 200
nmixtures = 200
backgroundRatio = 0.5
noiseSigma = 1

# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history,nmixtures,backgroundRatio,noiseSigma)
fgbg = cv2.createBackgroundSubtractorMOG2()


for i in range(1000):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame, learningRate)
    #bg = fgbg.getBackgroundImage()

    #cv2.imshow('bg',bg)
    cv2.imshow('fgmask',fgmask)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()