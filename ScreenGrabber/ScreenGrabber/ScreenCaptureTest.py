import nummpy as np
import cv2

import sys

print("hello")
cams_test = 10
for i in range(0, cams_test):
    cap = cv2.VideoCapture(i)
    test, frame = cap.read()
    print("i : "+str(i)+" /// result: "+str(test))

cap.release()
cv2.destroyAllWindows()