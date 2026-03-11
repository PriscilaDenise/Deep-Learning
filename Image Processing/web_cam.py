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

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    h, w = frame.shape[:2]
    output = frame.copy()

    if mode == "flip":
        output = cv2.flip(frame, 1)

    elif mode == "pan":
        tx, ty = 80, 40
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        output = cv2.warpAffine(frame, M, (w, h))

    elif mode == "zoom":
        zoomed = cv2.resize(frame, None, fx=1.5, fy=1.5)
        zh, zw = zoomed.shape[:2]

        # Crop center back to original size
        start_x = (zw - w) // 2
        start_y = (zh - h) // 2
        output = zoomed[start_y:start_y+h, start_x:start_x+w]

    elif mode == "shrink":
        small = cv2.resize(frame, None, fx=0.5, fy=0.5)
        sh, sw = small.shape[:2]

        # Put smaller image on black background of original size
        output = np.zeros_like(frame)
        x_offset = (w - sw) // 2
        y_offset = (h - sh) // 2
        output[y_offset:y_offset+sh, x_offset:x_offset+sw] = small

    elif mode == "rotate":
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, 30, 1.0)
        output = cv2.warpAffine(frame, M, (w, h))

    # Show video
    cv2.imshow("Webcam Live Processing", output)

    # Save processed frame
    out.write(output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('f'):
        mode = "flip"
    elif key == ord('p'):
        mode = "pan"
    elif key == ord('z'):
        mode = "zoom"
    elif key == ord('s'):
        mode = "shrink"
    elif key == ord('r'):
        mode = "rotate"
    elif key == ord('o'):
        mode = "original"
    elif key == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()