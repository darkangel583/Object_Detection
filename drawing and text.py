import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #img = cv2.line(frame, (0, 0), (width, height), (250, 0, 0), 10)
    #img = cv2.line(img, (0, height), (width, 0), (250, 0, 0), 10)

    #img = cv2.rectangle(frame, (50, 50), (500, 500), (255,0,0), 1)

    #img = cv2.circle(frame,(300, 300), 60, (0,0,255), 0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(frame, "Shashaank is a legend", (20,height - 10), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Video",img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()