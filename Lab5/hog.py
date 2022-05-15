import cv2
import numpy as np

# For HOG plot
from skimage import exposure
from skimage import feature

WINSIZE = (64, 128) # Must be this size because of the people detector
BLOCKSIZE = (16, 16)
BLOCKSTRIDE = (8, 8)
CELLSIZE = (8, 8)
BINS = 9
BOXCOLOR = (255, 0, 255)
BOXTHICKNESS = 3

cap = cv2.VideoCapture("../material/Video.mp4")

# Initialise multiscale HOG detector
hog = cv2.HOGDescriptor(
    WINSIZE, 
    BLOCKSIZE, 
    BLOCKSTRIDE, 
    CELLSIZE, 
    BINS
)

# Initialize people detector ((64, 128) default window)
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while cap.isOpened():
    ret, frame = cap.read()

    hogImage = frame.copy()

    (rects, weights) = hog.detectMultiScale(frame)
    for rect in rects:
        cv2.rectangle(
            frame, 
            (rect[0], rect[1]),
            (rect[0]+rect[2], rect[1]+rect[3]), 
            BOXCOLOR, 
            BOXTHICKNESS
        )

    # Compute HOG features for visualisation
    (H, hogImage) = feature.hog(hogImage, orientations=8, pixels_per_cell=(16, 16),
        cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",visualize=True)
    hogImage = exposure.rescale_intensity(hogImage, out_range=(50, 255))
    hogImage = hogImage.astype("uint8")

    cv2.imshow("HOG Image", hogImage)
    cv2.imshow("Hog detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break


