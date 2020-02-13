import numpy as np
import cv2

#import sys
#input = sys.argv[1]

cap = cv2.VideoCapture(2)

ret, frame = cap.read()

#cv2.imwrite("%s.jpg" % input, frame)
cv2.imwrite("test.jpg", frame)
 
cap.release()
cv2.destroyAllWindows()
