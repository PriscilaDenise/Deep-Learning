import cv2
import numpy as np

# Load image
image = cv2.imread("Image Processing/check.jpg")

# print(image)

if image is None:
    print("Error: Image not found.")
    exit()

# Get original height and width
h, w = image.shape[:2]

# 1. Flip
flip_horizontal = cv2.flip(image, 1) # mirror left-right
flip_vertical = cv2.flip(image, 0) # mirror up-down

# 2. Pan (translate image)
tx, ty = 100, 50 # move right by 100, down by 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
panned = cv2.warpAffine(image, translation_matrix, (w, h))

# 3. Zoom (scale up)
zoomed = cv2.resize(image, None, fx=1.5, fy=1.5)

# 4. Shrink (scale down)
shrunk = cv2.resize(image, None, fx=0.5, fy=0.5)

# 5. Rotate
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0) # angle 45 degrees
rotated = cv2.warpAffine(image, rotation_matrix, (w, h))

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Flip Horizontal", flip_horizontal)
cv2.imshow("Flip Vertical", flip_vertical)
cv2.imshow("Panned Image", panned)
cv2.imshow("Zoomed Image", zoomed)
cv2.imshow("Shrunk Image", shrunk)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()