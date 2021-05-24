import cv2
import numpy as np
from skimage import exposure
from skimage import feature

cap = cv2.VideoCapture("/home/mmlab/workspace/CVLaboratories/material/Video.mp4")

#initialise multiscale HOG detector
hog = cv2.HOGDescriptor((64, 128), (16, 16), (8, 8), (8, 8), 9)
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while cap.isOpened():
    ret, frame = cap.read()

    frame_copy = frame.copy()

    (rects, weights) = hog.detectMultiScale(frame)
    for rect in rects:
        cv2.rectangle(frame, (rect[0], rect[1]),
                      (rect[0]+rect[2], rect[1]+rect[3]), (255.0, 0.0, 255.0), thickness=3)

    #compute HOG features for visualisation
    (H, hogImage) = feature.hog(frame_copy, orientations=8, pixels_per_cell=(16, 16),
        cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",visualize=True)
    hogImage = exposure.rescale_intensity(hogImage, out_range=(50, 255))
    hogImage = hogImage.astype("uint8")

    cv2.imshow("HOG Image", hogImage)
    cv2.imshow("hog detected", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


