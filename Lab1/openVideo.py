import numpy as np
import cv2

webcam = False

if webcam:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture("../material/Video.mp4")

for i in range(1000):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If video end reached
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Frame',frame)
    cv2.imwrite(f'frames/frame_{i}.jpg',frame)
    
    # Wait and exit if q is pressed
    if cv2.waitKey(1) == ord('q') or not ret:
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()