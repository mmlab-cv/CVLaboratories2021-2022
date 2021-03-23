import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("/home/mmlab/workspace/CVLaboratories/material/Video.mp4")

for i in range(100):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imwrite('img'+str(i)+'.jpg',frame)
    cv2.waitKey(1)


# When everything done, release the capture
cap.release()