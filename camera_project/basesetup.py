import cv2
from datetime import datetime

cap = cv2.VideoCapture(1)
out = cv2.VideoWriter('output.avi', -1, 20.0, (1080, 1920))

while True:

    ret, image = cap.read()

    # print(image.shape)
    if ret:
        cv2.imshow("My camera", image)
        out.write(image)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break

    if key == ord("c"):
        now = datetime.now()
        date_time = now.strftime("%Y_%m_%d__%H:%M:%S")
        print(date_time)
        cv2.imwrite("{}.png".format(date_time), image)


cap.release()
cv2.destroyAllWindows()
out.release()
