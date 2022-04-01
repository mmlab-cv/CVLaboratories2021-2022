import numpy as np
import cv2

frames = []
N = 1
MAX_FRAMES = 1000
THRESH = 50
MAXVAL = 255

webcam = True

if webcam:
    cap = cv2.VideoCapture(1)
else:
    cap = cv2.VideoCapture("../material/Video.mp4")

for t in range(MAX_FRAMES):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If video end reached
    if not ret:
        break
    
    # Convert frame to grayscale and append to list of frames
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(frame_gray)

    if t >= N:
        # D(N) = || I(t) - I(t+N) || = || I(t-N) - I(t) ||
        diff = cv2.absdiff(frames[t-N], frames[t])

        # Mask thresholding
        ret, motion_mask = cv2.threshold(diff, THRESH, MAXVAL, cv2.THRESH_BINARY)

        cv2.imshow('Motion mask', motion_mask)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Wait and exit if q is pressed
    if cv2.waitKey(1) == ord('q') or not ret:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()