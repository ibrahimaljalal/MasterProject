#Nots:

#1-this will be a test code for the Arduino
#2-This file could also work without Arduino 

import cv2 as cv
import numpy as np
import copy


#############################################################
#p stands for parameters. the parameters 
#will be different depending on the task
##########################################

p={
'H_U':180,
'H_L':80,

'S_U':80,
'S_L':0,

'V_U':255,
'V_L':0,

'Gaussian_Blur':0,

'trackbarHSVHight':200,

'trackbarHSVWidth':300,

#########################

'cameraNumber': 1,
'waitKey': 50,
'keyNumber': 27,

'defaultResolution': True,
'cameraResolutionWidth': 160, 
'cameraResolutionHight': 120,

'frameXSize': 480,
'frameYSize': 360,

'showFrames':True,

'blurBefore':True,

'areaPercentage':0.01

}

#This the most important function
#############################################################
def findCenters(frame,areaPercentage,originalFrame,drawResults=False):

    originalCopy=copy.deepcopy(originalFrame)

    contours, hierarchy = cv.findContours(frame, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    

    sortedC=sorted(contours,key=cv.contourArea,reverse=False)

    sortedC=sortedC[::-1]

    allPixels=frame.shape[0]*frame.shape[1]

    try:
        con=sortedC[0]

        area=cv.contourArea(con)

        conPercentage=area/allPixels

        if conPercentage>=areaPercentage:

            M=cv.moments(con)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            if drawResults==True:
                cv.drawContours(originalCopy,con,-1,(0,0,50),3)

                x,y,w,h=cv.boundingRect(con)

                originalCopy=cv.rectangle(originalCopy,(x,y),(x+w,y+h),(0,50,0),3)

                cxRect=x+w/2
                cyRect=y+h/2

                originalCopy=cv.circle(originalCopy,(int(cx),int(cy)),radius=2,color=(0,0,255),thickness=-1)

                originalCopy=cv.circle(originalCopy,(int(cxRect),int(cyRect)),radius=2,color=(0,255,0),thickness=-1)


        centroids=[cx,cy]

        if drawResults==True:
            return centroids,originalCopy


        return centroids

    except:
        return [None,None], originalFrame

    

#############################################################


#This simple program will covert from pixels x and y pixels to percentage
#Note: the x and y will start fom the buttom left
#############################################################
def convertFromXYPixelsToPercentage(cx,cy,frame):
    
    try:
        xp=cx/frame.shape[1]
        yp=1-cy/frame.shape[0]

        return [xp,yp]
    except:    
        return [None,None]

#############################################################




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


#Camera resolution
if p['defaultResolution']==False:
    cap.set(3,p['cameraResolutionWidth'])
    cap.set(4,p['cameraResolutionHight'])




#Function for the trackbar
def forTrackBar(x):
    pass

#setting the trackbars
cv.namedWindow("Trackbars",cv.WINDOW_FREERATIO)

cv.createTrackbar('H_U',"Trackbars",0,179,forTrackBar)

cv.createTrackbar('H_L',"Trackbars",0,179,forTrackBar)

cv.createTrackbar('S_U',"Trackbars",0,255,forTrackBar)

cv.createTrackbar('S_L',"Trackbars",0,255,forTrackBar)

cv.createTrackbar('V_U',"Trackbars",0,255,forTrackBar)

cv.createTrackbar('V_L',"Trackbars",0,255,forTrackBar)

cv.createTrackbar('Gaussian_Blur',"Trackbars",0,100,forTrackBar)


#Trackbars defult values

cv.setTrackbarPos('H_U',"Trackbars",p['H_U'])

cv.setTrackbarPos('H_L',"Trackbars",p['H_L'])

cv.setTrackbarPos('S_U',"Trackbars",p['S_U'])

cv.setTrackbarPos('S_L',"Trackbars",p['S_L'])

cv.setTrackbarPos('V_U',"Trackbars",p['V_U'])

cv.setTrackbarPos('V_L',"Trackbars",p['V_L'])

cv.setTrackbarPos('Gaussian_Blur',"Trackbars",p['Gaussian_Blur'])


trackbarHSV=np.zeros((p['trackbarHSVHight'],p['trackbarHSVWidth'],3),np.uint8)

#This will be useful if do not want to show the frames
p['H_U']=cv.getTrackbarPos("H_U","Trackbars")

p['H_L']=cv.getTrackbarPos("H_L","Trackbars")

p['S_U']=cv.getTrackbarPos("S_U","Trackbars")

p['S_L']=cv.getTrackbarPos("S_L","Trackbars")

p['V_L']=cv.getTrackbarPos("V_L","Trackbars")

p['V_U']=cv.getTrackbarPos("V_U","Trackbars")

p['Gaussian_Blur']=cv.getTrackbarPos("Gaussian_Blur","Trackbars")



while True:

    ret,frame=cap.read()

    frame=cv.resize(frame,(p['frameXSize'],p['frameYSize']))
    
    hsvframe=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    

    if p['showFrames']==True:
        
        #For trackbars
        p['H_U']=cv.getTrackbarPos("H_U","Trackbars")

        p['H_L']=cv.getTrackbarPos("H_L","Trackbars")

        p['S_U']=cv.getTrackbarPos("S_U","Trackbars")

        p['S_L']=cv.getTrackbarPos("S_L","Trackbars")

        p['V_L']=cv.getTrackbarPos("V_L","Trackbars")

        p['V_U']=cv.getTrackbarPos("V_U","Trackbars")

        p['Gaussian_Blur']=cv.getTrackbarPos("Gaussian_Blur","Trackbars")


        trackbarHSV[:,:int(p['trackbarHSVWidth']/2)]=(p['H_L'],p['S_L'],p['V_L'])
        trackbarHSV[:,int(p['trackbarHSVWidth']/2):]=(p['H_U'],p['S_U'],p['V_U'])

        trackbarHSV[:,:int(p['trackbarHSVWidth']/2)]=cv.cvtColor(trackbarHSV[:,:int(p['trackbarHSVWidth']/2)],cv.COLOR_HLS2BGR)
        trackbarHSV[:,int(p['trackbarHSVWidth']/2):]=cv.cvtColor(trackbarHSV[:,int(p['trackbarHSVWidth']/2):],cv.COLOR_HLS2BGR)

        
        
        if p['blurBefore']==True:

            filtered=cv.GaussianBlur(frame,(2*p['Gaussian_Blur']+1,2*p['Gaussian_Blur']+1),0)

            hsvMask=cv.inRange(filtered,(p['H_L'],p['S_L'],p['V_L']),(p['H_U'],p['S_U'],p['V_U']))
            
           
            cv.imshow("Original Frame: 1",frame)

            cv.imshow("Filtered: 2",filtered)

            cv.imshow("HSV mask: 3",hsvMask)

            centroids,resultFrame=findCenters(hsvMask,p['areaPercentage'],frame,True)

            toArduino=convertFromXYPixelsToPercentage(centroids[0],centroids[1],frame)

            print(toArduino)


            #print(centroids)

            cv.imshow("Result: 4", resultFrame)
            
            cv.imshow("Trackbars",trackbarHSV)

        else:

            hsvMask=cv.inRange(hsvframe,(p['H_L'],p['S_L'],p['V_L']),(p['H_U'],p['S_U'],p['V_U']))

            filtered=cv.GaussianBlur(hsvMask,(2*p['Gaussian_Blur']+1,2*p['Gaussian_Blur']+1),0)


            cv.imshow("Original Frame: 1",frame)

            cv.imshow("HSV mask: 2",hsvMask)

            cv.imshow("Filtered: 3",filtered)

            centroids,resultFrame=findCenters(filtered,p['areaPercentage'],frame,True)

            print(centroids)

            cv.imshow("Result: 4", resultFrame)
            
            cv.imshow("Trackbars",trackbarHSV)

        


        if cv.waitKey(p['waitKey'])==p['keyNumber']:
            break


    else:

        if p['blurBefore']==True:
            filtered=cv.GaussianBlur(frame,(2*p['Gaussian_Blur']+1,2*p['Gaussian_Blur']+1),0)

            hsvMask=cv.inRange(filtered,(p['H_L'],p['S_L'],p['V_L']),(p['H_U'],p['S_U'],p['V_U']))

            centroids,resultFrame=findCenters(hsvMask,p['areaPercentage'],frame,False)

            print(centroids)

        else:
            hsvMask=cv.inRange(hsvframe,(p['H_L'],p['S_L'],p['V_L']),(p['H_U'],p['S_U'],p['V_U']))

            filtered=cv.GaussianBlur(hsvMask,(2*p['Gaussian_Blur']+1,2*p['Gaussian_Blur']+1),0)

            centroids,resultFrame=findCenters(filtered,p['areaPercentage'],frame,False)

            print(centroids)



cap.release()
cv.destroyAllWindows()