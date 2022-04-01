import cv2

# Define (relative) path to the image
image_path = "../material/OpenCV.png"

# Define how to read the image (color, grayscale, color + alpha)
image_flag = cv2.IMREAD_UNCHANGED

# cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
# cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
# cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.

image = cv2.imread(image_path, image_flag)
print(f"Image shape: {image.shape}")
print(f"Image dtype: {image.dtype}")

# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('My beautiful title', image)
cv2.waitKey(0)
