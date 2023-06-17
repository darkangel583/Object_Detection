import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    tag = cv2.resize(frame, (160, 120))
    #print(tag.shape)
    #print(frame.shape)
    frame[:height//4, :width//4] = tag
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()