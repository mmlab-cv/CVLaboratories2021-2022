import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("/home/mmlab/workspace/CVLaboratories/material/Video.mp4")

frame_index = 0
while cap.isOpened():
    #read video
    ret, frame = cap.read()

    #copy frame and convert to grayscale
    frame_copy = frame.copy()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Select GFF Features
    if frame_index % 30 == 0:
        corners = cv2.goodFeaturesToTrack(frame_gray, maxCorners=100,
            qualityLevel=0.01,
            minDistance=10,
            blockSize=3,
            useHarrisDetector=False,
            k=0.04)
    else:
        #Track GFF features with Lucas-Kanade optical flow
        corners, status, err = cv2.calcOpticalFlowPyrLK(prev_frame, frame, prev_corners, None)

    #plot keypoints
    np_corners = np.int0(corners)
    for i,crn in enumerate(np_corners):
        x, y = crn.ravel()
        cv2.circle(frame_copy, (x, y), 3, np.array([i, 2*i, 255-i], float))

    #copy values for next iteration 
    prev_frame, prev_corners = frame.copy(), corners

    #plot results
    cv2.imshow('gff', frame_copy)
    if cv2.waitKey(1) & 0xFF == ord('q'): #close video is q is pressed
        break

    frame_index += 1

cap.release()
cv2.destroyAllWindows()