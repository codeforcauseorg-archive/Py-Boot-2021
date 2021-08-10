import cv2
import numpy as np
cap = cv2.VideoCapture(1)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)

        for face in faces:
            [x, y, w, h] = face

            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("my frame", frame)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break

