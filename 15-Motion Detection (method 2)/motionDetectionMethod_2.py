#This file is completely independent

import numpy as np
import cv2 as cv
import time
import datetime

#########################################################################
#########################################################################

#p stands for parameters. the parameters 
#will be different depending on the task
##########################################

p={

'cameraNumber': 1,
'waitKey': 50,
'keyNumber': 27,

'defaultResolution': True,
'cameraResolutionWidth': 160, 
'cameraResolutionHight': 120,

'frameXSize': 500,
'frameYSize': 500,

"History":2000


}

#This code will catch the camera even if the camera number is wrong
#############################################################
while True:

        cap=cv.VideoCapture(p['cameraNumber'])
        if (cap.isOpened()==True):
            break

        if (cap.isOpened()==False and p['cameraNumber']>=0):
            p['cameraNumber']=p['cameraNumber']-1
        if (cap.isOpened()==False and p['cameraNumber']<0):
            p['cameraNumber']=p['cameraNumber']+1

if p['defaultResolution']==False:
    cap.set(3,p['cameraResolutionWidth'])
    cap.set(4,p['cameraResolutionHight'])
#############################################################


#############################################################
if p['defaultResolution']==False:
    cap.set(3,p['cameraResolutionWidth'])
    cap.set(4,p['cameraResolutionHight'])
#############################################################


subtractor=cv.createBackgroundSubtractorMOG2(history=p['History'])

while True:

    _, frame=cap.read()

    frame=cv.resize(frame,(p['frameXSize'],p['frameYSize']))

    method2Motion=subtractor.apply(frame)

    cv.imshow("Original",frame)
    cv.imshow("Motion Detection",method2Motion)




    if cv.waitKey(p['waitKey'])==p['keyNumber']:
            break






cap.release()
cv.destroyAllWindows()