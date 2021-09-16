import os
import orthographicTransorm as ot
import cv2 as cv

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)


cam=cv.VideoCapture(0)

while True:
    _,frame=cam.read()
    ot.p["rectangleStartingCoordinates"]
    out=ot.transform(frame)
    cv.imshow("Testing",out)

    if cv.waitKey(50)==27:
        break

cam.release()
cv.destroyAllWindows()









