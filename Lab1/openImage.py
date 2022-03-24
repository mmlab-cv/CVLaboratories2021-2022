import cv2

image_path = "../material/Google.jpg"
image = cv2.imread(image_path, 1)

cv2.imshow('My beautiful title', image)
cv2.waitKey(0)
