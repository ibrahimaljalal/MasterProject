# sudo apt-get install libzbar0
# pip3 install pyzbar
# pip3 install opencv-python
# pip3 install opencv-contrib-python

#Notes:
#We could also use barcods
#This does not work very well with Windows

import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode
import datetime

#########################################################################
#########################################################################

#p stands for parameters. the parameters 
#will be different depending on the task
##########################################

p={

'cameraNumber': 2,
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

        for barcode in decode(frame):
            myData = barcode.data.decode('utf-8')

            now = datetime.datetime.now()
            #"%y-%m-%D  %H:%M:%S" (for strftime)
            print("")
            print(myData+ "  "+"Time: "+now.strftime("%y-%m-%D  %H:%M:%S"))
            print("")

            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv.polylines(frame,[pts],True,(0,0,255),5)

            pts2 = barcode.rect
            cv.putText(frame,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2)

        cv.imshow("Result Frame",frame)


    else:
        for barcode in decode(frame):
            myData = barcode.data.decode('utf-8')

            now = datetime.datetime.now()
            #"%y-%m-%D  %H:%M:%S" (for strftime)
            print("")
            print(myData+ "  "+"Time: "+now.strftime("%y-%m-%D  %H:%M:%S"))
            print("")

    if cv.waitKey(p['waitKey'])==p['keyNumber']:
            break


cap.release()
cv.destroyAllWindows()    

