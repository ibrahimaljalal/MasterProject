from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import datetime
import time



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

'showFrames': True,
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

while True:
    ret,frame=cap.read()
    frame=cv.resize(frame,(p['frameXSize'],p['frameYSize']))

    if p['showFrames']==True:

        cv.imshow("Text Detection",frame)
        print(pytesseract.image_to_string(frame,lang="eng"))



    else:

        print(pytesseract.image_to_string(frame,lang="eng"))
       

    if cv.waitKey(p['waitKey'])==p['keyNumber']:
            break


cap.release()
cv.destroyAllWindows()    