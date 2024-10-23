from CONST import CV_PATH
from object_detection import ObjectDetector
import cv2
import os

# Load the object detector
detector = ObjectDetector(model_path=os.path.join(CV_PATH, 'models', 'yolo11m.pt'))

# Open a connection to the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Use the detector on the frame
    boxes, grasp_info = detector.detect(frame)

    # Draw detections on the frame
    annotated_frame = detector.annotate_frame(frame, boxes, grasp_info=grasp_info)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

# Destroy all windows
cv2.destroyAllWindows()