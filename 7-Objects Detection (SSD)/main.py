import objectsDetection as od
import cv2 as cv
import os

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

#od.p["showFrames"]=False
if od.p["showFrames"]==True:
    cam=cv.VideoCapture(1)
    while True:
        _,frame=cam.read()
        output=od.objectsAvailable(frame)
        cv.imshow("Searching for Objects",output)
        if cv.waitKey(50)==27:
            break
    cam.release()
    cv.destroyAllWindows()

else:
    cam=cv.VideoCapture(1)
    while True:
        _,frame=cam.read()
        if cv.waitKey(50)==27:
            break
        print(od.objectsAvailable(frame))
        




