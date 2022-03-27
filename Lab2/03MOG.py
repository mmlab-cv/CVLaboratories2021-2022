import numpy as np
import cv2

MAX_FRAMES = 1000
LEARNING_RATE = -1
HISTORY = 200
N_MIXTURES = 200
BACKGROUND_RATIO = 0.5
NOISE_SIGMA = 1

webcam = False

if webcam:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture("../material/Video.mp4")

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(HISTORY, N_MIXTURES, BACKGROUND_RATIO, NOISE_SIGMA)
# fgbg = cv2.createBackgroundSubtractorMOG2()


for i in range(MAX_FRAMES):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If video end reached
    if not ret:
        break

    fgmask = fgbg.apply(frame, LEARNING_RATE)
    #bg = fgbg.getBackgroundImage()

    #cv2.imshow('bg',bg)
    cv2.imshow('fgmask',fgmask)
    cv2.imshow('frame',frame)

    # Wait and exit if q is pressed
    if cv2.waitKey(1) == ord('q') or not ret:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()