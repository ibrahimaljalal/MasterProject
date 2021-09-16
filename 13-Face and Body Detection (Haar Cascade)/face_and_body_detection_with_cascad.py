import cv2 as cv
import numpy as np
import os

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)


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

'frameXSize': 800,
'frameYSize': 500,

'showFrames': True,

'detect Face': True,

'detect body': True,

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

face=cv.CascadeClassifier("face.xml")

body=cv.CascadeClassifier("fullbody.xml")

while True:
    ret,frame=cap.read()
    frame=cv.resize(frame,(p['frameXSize'],p['frameYSize']))

    grayFrame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    if p['detect Face']==True:
        faces=face.detectMultiScale(grayFrame,1.3,5)

        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    if p['detect body']==True:
        bodies=body.detectMultiScale(grayFrame,1.3,5)

        for (x,y,w,h) in bodies:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    

    
    cv.imshow("Face/Body Detection",frame)
    
    if cv.waitKey(p['waitKey'])==p['keyNumber']:
        break

cap.release()
cv.destroyAllWindows()