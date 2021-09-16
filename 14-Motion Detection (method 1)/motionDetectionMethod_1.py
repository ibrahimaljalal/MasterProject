#This file is completely independent
import numpy as np
import cv2 as cv
import time
import datetime
import os

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

'Gaussian_Blur':0,

'Threshold':20,

'Dilate_Iterations':3,

'Area_Percentage':0.01,

'B&W_Mask':"mask2.png",

"With_Mask" : True

}

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

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

ret,frame1=cap.read()
frame1=cv.resize(frame1,(p['frameXSize'],p['frameYSize']))

ret,frame2=cap.read()
frame2=cv.resize(frame2,(p['frameXSize'],p['frameYSize']))

mask=cv.imread(p['B&W_Mask'])
mask=cv.resize(mask,(p['frameXSize'],p['frameYSize']))
mask=cv.cvtColor(mask,cv.COLOR_BGR2GRAY)

while True:

    diff=cv.absdiff(frame1,frame2)

    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)

    filtered=cv.GaussianBlur(gray,(2*p['Gaussian_Blur']+1,2*p['Gaussian_Blur']+1),0)

    _, thresh=cv.threshold(filtered,p['Threshold'] ,255,cv.THRESH_BINARY)

    dilated=cv.dilate(thresh,None,p['Dilate_Iterations'])

    

    if p["With_Mask"]==True:


        withMask=cv.bitwise_and(dilated,mask)
    
        contours, _= cv.findContours(withMask, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv.contourArea(contour)>=p['Area_Percentage']*frame1.shape[0]*frame1.shape[1]:
                
                now = datetime.datetime.now()
                
                #"%y-%m-%D  %H:%M:%S" (for strftime)
                print("Motion Detected at "+now.strftime("%y-%m-%D  %H:%M:%S"))

    else:

        contours, _= cv.findContours(dilated, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv.contourArea(contour)>=p['Area_Percentage']*frame1.shape[0]*frame1.shape[1]:
                
                now = datetime.datetime.now()
                
                #"%y-%m-%D  %H:%M:%S" (for strftime)
                print("Motion Detected at "+now.strftime("%y-%m-%D  %H:%M:%S"))


    
    if p['showFrames']==True:

        cv.imshow("Original Frame: 1",frame1)
        cv.imshow("Difference and Filtered Frame: 2",filtered)
        cv.imshow("Threshold: 3",thresh)
        cv.imshow("Dilated: 4",dilated)

        if p["With_Mask"]==True:
            cv.imshow("With Mask: 5",withMask)




    frame1=frame2

    ret,frame2=cap.read()
    frame2=cv.resize(frame2,(p['frameXSize'],p['frameYSize']))

    
    if cv.waitKey(p['waitKey'])==p['keyNumber']:
            break


cap.release()
cv.destroyAllWindows()