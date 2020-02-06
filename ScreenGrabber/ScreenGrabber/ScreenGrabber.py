import numpy as np
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

ret, frame = cap.read()

cv2.imwrite("image.jpg", frame)
   
cap.release()
cv2.destroyAllWindows()