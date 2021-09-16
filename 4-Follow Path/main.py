import followPath
import cv2 as cv
import os

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

#followPath.p["showFrames"]=False
if followPath.p["showFrames"]==True:
    cam=cv.VideoCapture(1)
    while True:
        _,frame=cam.read()
        results=followPath.getAngle(frame)
        cv.imshow("1-Frame",results[0])
        cv.imshow("2-Frame Filtered",results[1])
        cv.imshow("3-HSV Range",results[2])
        cv.imshow("4-Erosion/Dilation",results[3])
        cv.imshow("5-Illustration",results[4])
        if cv.waitKey(50)==27:
            break
    cam.release()
    cv.destroyAllWindows()

else:
    cam=cv.VideoCapture(1)
    while True:
        _,frame=cam.read()
        print(followPath.getAngle(frame))

        if cv.waitKey(50)==27:
            break
    cam.release()
    cv.destroyAllWindows()

