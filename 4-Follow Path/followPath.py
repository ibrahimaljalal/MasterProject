import cv2 as cv
import numpy as np
import math
import copy

#Note make sure that showFrames is False when you want to apply the code
p={

"baseFraction":0.1,
"histogramFraction":0.1,

"hsvLower":[90,55,55],
"hsvUpper":[140,255,255],

#square Matrix
"kernelSize":10,
"kernelFactor":0.04,

"dilate":4,
"erode":15,
#if applyErode is True dilate and if it is False erode will not have any effect
"applyErode":True,

"showFrames":True,

"PrintAngle":True
}
# in hsv h from 0 to 179 and s, and v are from 0 to 255
#in inRange function firs h ,s and v

def getHist(im,min=p["histogramFraction"]):

    try:
        npSum=np.sum(im,axis=0)
        minVal=math.ceil(im.shape[0]*min)*255
        
        indexArray=np.where(npSum>=minVal)
        average=np.average(indexArray)


        return int(average)
    except ValueError:
        return None

def getAngle(frame):
    while True:
        angle = None
            
        #https://www.youtube.com/watch?v=u3poUhCxx4k
        kernel=np.ones((p["kernelSize"],p["kernelSize"]),np.float32)*p["kernelFactor"]
        
        filterImg=cv.filter2D(frame,-1,kernel)


        hsvImg=cv.cvtColor(filterImg,cv.COLOR_BGR2HSV)

        hsvLower=np.array(p["hsvLower"], np.uint8)
        hsvUpper=np.array(p["hsvUpper"], np.uint8)
        #hsvMask is a black and white image
        hsvMask=cv.inRange(hsvImg,hsvLower,hsvUpper)

        #https://www.youtube.com/watch?v=xSzsD4kXhRw

        if p["applyErode"]!=True:
            dilateKernel=np.ones((p["dilate"],p["dilate"]),np.uint8)
            erodOrDilate=cv.dilate(hsvMask,dilateKernel)

        if p["applyErode"]==True:
            erodeKernel=np.ones((p["erode"],p["erode"]),np.uint8)
            erodOrDilate=cv.erode(hsvMask,erodeKernel)

        #main part for the path
        ##############################
        lowImg=erodOrDilate[math.floor(erodOrDilate.shape[0]*(1-p["baseFraction"])):]

        resultLow=getHist(lowImg)
        resulAll=getHist(erodOrDilate)

        #Angle is positive from the right
        if (resultLow is not None) and (resulAll is not None):
            angle=90-math.degrees(math.atan2(erodOrDilate.shape[0],resultLow-resulAll))
            if p["PrintAngle"]==True:
                print("{:.2f}".format(angle)+" degrees")
          

        if p["showFrames"]==True:

            illustration=copy.deepcopy(erodOrDilate)
            
            if resultLow is not None:
                cv.line(illustration,(resultLow,illustration.shape[0]),(resultLow,0),(255,0,0),thickness=10)
            if resulAll is not None:
                cv.line(illustration,(resulAll,illustration.shape[0]),(resulAll,0),(255,0,0),thickness=2)
            
            return [frame,filterImg,hsvMask,erodOrDilate,illustration]

        else:
            return angle




    




            


   