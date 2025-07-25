import cv2
import numpy as np

cap = cv2.VideoCapture('../../source/input1.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners = cv2.goodFeaturesToTrack(gray,
                                      maxCorners=200,
                                      qualityLevel=0.01,
                                      minDistance=10)
    if corners is not None:
        corners = corners.astype(int)
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    cv2.imshow('original video', gray)
    cv2.imshow('shi_tomasi video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

