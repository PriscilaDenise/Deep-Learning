import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get frame size for saving video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20.0

# Save processed video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('processed_video.avi', fourcc, fps, (frame_width, frame_height))

mode = "original"

print("Press keys to change effect:")
print("f = flip")
print("p = pan")
print("z = zoom")
print("s = shrink")
print("r = rotate")
print("o = original")
print("q = quit")

