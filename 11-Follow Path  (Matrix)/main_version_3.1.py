#This file is completely independent

import numpy as np
import cv2 as cv
import sys


#########################################################################
#########################################################################

#p stands for parameters. the parameters 
#will be different depending on the task
##########################################

p={'illustrationColorWidth':400,
'illustrationColorHight':100,

'trackbarsWindowWidth':400,
'trackbarsWindowHight':100,

'hueLow':1,
'saturationLow':0,
'valueLow':0,

'hueUp':0,
'saturationUp':255,
'valueUp':255,



'showSegmentation':True,
'bInBGRColor':0,
'gInBGRColor':0,
'rInBGRColor':255,

'thickness':2,

#blureValue
'gaussianBlurValue':0,

'erodeNumber':0,
'erodeIterations':0,

'ySegments':10,
'xSegments':10,

'areaFraction':0.1,


############################################

'cameraNumber': 1,
'waitKey': 50,
'keyNumber': 27,

#Make sure to make the width and hight in right proportion
#The least for my camera seems to be 160*120 
#(if you lower it you will get an error)
'defaultResolution': True,
'cameraResolutionWidth': 160, 
'cameraResolutionHight': 120,

'frameXSize': 222,
'frameYSize': 222,

'showFrames': True

}



#########################################################################
#########################################################################


#This part should not be changed
##########################################
pKeys=list(p)

try:
    if sys.argv[1]=="show":
        for i in range(len(pKeys)):
                print("Argument "+str(i+1)+": name: "\
                +str(pKeys[i])+\
                ",  value: "+str(p[pKeys[i]]))
        
except:
    pass
else:
    sys.exit()


try:
    if sys.argv[1]=="help":
        pass
        
        
except:
    pass
else:
    sys.exit()        



if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        p[pKeys[i-1]]=sys.argv[i]

for i in range(len(pKeys)):
            print("Argument "+str(i+1)+": name: "\
            +str(pKeys[i])+\
            ",  value: "+str(p[pKeys[i]]))

print("\n")


##########################################


#Make sure to give your parameters the right type
##########################################
p['illustrationColorWidth']=int(p['illustrationColorWidth'])
p['illustrationColorHight']=int(p['illustrationColorHight'])

p['trackbarsWindowWidth']=int(p['trackbarsWindowWidth'])
p['trackbarsWindowHight']=int(p['trackbarsWindowHight'])

p['hueLow']=int(p['hueLow'])
p['saturationLow']=int(p['saturationLow'])
p['valueLow']=int(p['valueLow'])

p['hueUp']=int(p['hueUp'])
p['saturationUp']=int(p['saturationUp'])
p['valueUp']=int(p['valueUp'])

p['showSegmentation']=bool(p['showSegmentation'])
p['bInBGRColor']=int(p['bInBGRColor'])
p['gInBGRColor']=int(p['gInBGRColor'])
p['rInBGRColor']=int(p['rInBGRColor'])
p['thickness']=int(p['thickness'])


p['gaussianBlurValue']=int(p['gaussianBlurValue'])
p['erodeNumber']=int(p['erodeNumber'])
p['erodeIterations']=int(p['erodeIterations'])

p['ySegments']=int(p['ySegments'])
p['xSegments']=int(p['xSegments'])





p['cameraNumber']=int(p['cameraNumber'])
p['waitKey']=int(p['waitKey'])
p['keyNumber']=int(p['keyNumber'])

p['defaultResolution']=bool(p['defaultResolution'])
p['cameraResolutionWidth']=int(p['cameraResolutionWidth'])
p['cameraResolutionHight']=int(p['cameraResolutionHight'])


p['frameXSize']=int(p['frameXSize'])
p['frameYSize']=int(p['frameYSize'])

p['showFrames']=bool(p['showFrames'])

p['areaFraction']=float(p['areaFraction'])

##########################################

#############################################################





def frameSegmentation(frame,ySegments,xSegments,\
    inputType="uint8",outputType='uint8'):
        
        frame=np.array(frame,dtype=inputType)

        frameShape=frame.shape
        
        if (len(frameShape) == 2 or len(frameShape) ==3):
            yPixels=frameShape[0]
            xPixels=frameShape[1]
            
            yPixelsYSegment=yPixels//ySegments
            xPixelsXSegment=xPixels//xSegments
            

        else:
            print("""Wrong frame format (frame should be either 
            n*m gray or n*m*3 colored image matrix)""")
            return None

        if len(frameShape)==2:
            allSegments=np.zeros((ySegments,xSegments,\
            yPixelsYSegment,xPixelsXSegment),dtype=outputType)

        elif len(frameShape)==3:
            allSegments=np.zeros((ySegments,xSegments,\
            yPixelsYSegment,xPixelsXSegment,3),dtype=outputType)
        
        

        for j in range(ySegments):
            for i in range(xSegments):
                allSegments[j,i]=frame[j*yPixelsYSegment:\
                yPixelsYSegment*(j+1),i*xPixelsXSegment:\
                xPixelsXSegment*(i+1)]

        return allSegments


def drawSegments(frame,ySegments,xSegments,\
        bgrColor=(255,0,0),thickness=5,inputType="uint8"):
        
        frame=np.array(frame,dtype=inputType)

        frameShape=frame.shape
        
        if (len(frameShape) == 2 or len(frameShape) ==3):
            yPixels=frameShape[0]
            xPixels=frameShape[1]
            

            xPixelsXSegment=xPixels//xSegments
            yPixelsYSegment=yPixels//ySegments

        else:
            print("""Wrong frame format (frame should be either 
            n*m gray or n*m*3 colored image matrix)""")
            return None

        yAxisLines=[i*xPixelsXSegment for i in range(1,xSegments)]
        xAxisLines=[i*yPixelsYSegment for i in range(1,ySegments)]


        for i in yAxisLines:
            frame=cv.line(frame,(i,0),(i,yPixels),bgrColor,p['thickness'])

        for i in xAxisLines:
            frame=cv.line(frame,(0,i),(xPixels,i),bgrColor,p['thickness'])


        return frame



def getPlace(bwframe,ySegments,xSegments,\
    areaFraction=0.1,detectWhat="HSV Range"):
            segmintPixels=(bwframe.shape[0]//ySegments)*\
            (bwframe.shape[1]//xSegments)

            indices=[detectWhat]

            allTheSegments=frameSegmentation(\
            bwframe,ySegments,xSegments)
            for j in range(allTheSegments.shape[0]):
                for i in range(allTheSegments.shape[1]):
                 contours, hierarchy =  cv.findContours(\
                    allTheSegments[j,i],cv.RETR_TREE,cv.\
                    CHAIN_APPROX_NONE)
                 for contour in  contours:
                     if cv.contourArea(contour)>areaFraction*\
                     segmintPixels:
                         indices.append([j,i])
                         break


            return indices

def convertToXY(row,col,ySegments,xSegments):
        if(col<xSegments and row<ySegments):
            x=col+1
            y=ySegments-row
            return x,y
        else:
            print("cordinats numbers out of range")
            return None



def convertToXYList(listNumpy,ySegments,xSegments):
        listResult=[]

        for i in range(len(listNumpy)):
            Result=convertToXY(listNumpy[i][0],\
            listNumpy[i][1],ySegments,xSegments)
            listResult.append(Result)

        return listResult



#for illustration
#############################################################
def convertFromXY(x,y,ySegments,xSegments):
        
        if (x<=xSegments and y<=ySegments):
            row=ySegments-y
            col=x-1

        return int(row),int(col)


def convertFromXYList(listXY,ySegments,xSegments):

    listResult=[]

    for i in range(len(listXY)):
            Result=convertFromXY(listXY[i][0],listXY[i][1],ySegments,xSegments)
            listResult.append(Result)

    return listResult


def resultIllustrationFrame(ySegments,xSegments,result,hight,width):
    

    numpyWhite=convertFromXYList(result,ySegments,xSegments)

    
    illustration=np.zeros((ySegments,xSegments),dtype='uint8')

    for i in range(len(numpyWhite)):
        illustration[numpyWhite[i][0],numpyWhite[i][1]]=255

    
    illustration=cv.resize(illustration,(width,hight),interpolation=cv.INTER_AREA)


    return illustration









def doNothing(x):
    pass




img=np.zeros((p['illustrationColorHight'],p['illustrationColorWidth'],3),np.uint8)

cv.namedWindow("Trackbars",cv.WINDOW_FREERATIO)
cv.resizeWindow("Trackbars",p['trackbarsWindowWidth'],p['trackbarsWindowHight'])

cv.createTrackbar("Hue Upper Limit","Trackbars",0,179,doNothing)

cv.createTrackbar("Hue Lower Limit","Trackbars",0,179,doNothing)

cv.createTrackbar("Saturation Upper Limit","Trackbars",0,255,doNothing)

cv.createTrackbar("Saturation Lower Limit","Trackbars",0,255,doNothing)

cv.createTrackbar("Value Upper Limit","Trackbars",0,255,doNothing)

cv.createTrackbar("Value Lower Limit","Trackbars",0,255,doNothing)

cv.createTrackbar("Gaussian Blur","Trackbars",0,100,doNothing)

cv.createTrackbar("Erode Number","Trackbars",0,100,doNothing)

cv.createTrackbar("Erode Iterations","Trackbars",0,100,doNothing)

#Setting the Trackbar
############################################################################
cv.setTrackbarPos("Hue Upper Limit","Trackbars",6)




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
#############################################################


if p['defaultResolution']==False:
    cap.set(3,p['cameraResolutionWidth'])
    cap.set(4,p['cameraResolutionHight'])




if p['defaultResolution']==False:
    cap.set(3,p['cameraResolutionWidth'])
    cap.set(4,p['cameraResolutionHight'])



#Setting default Trackbars 

cv.setTrackbarPos("Hue Lower Limit","Trackbars", p['hueLow'])

cv.setTrackbarPos("Saturation Lower Limit","Trackbars", p['saturationLow'])

cv.setTrackbarPos("Value Lower Limit","Trackbars", p['valueLow'])

cv.setTrackbarPos("Hue Upper Limit","Trackbars", p['hueUp'])

cv.setTrackbarPos("Saturation Upper Limit", "Trackbars", p["saturationUp"])

cv.setTrackbarPos("Value Upper Limit", "Trackbars", p["valueUp"])

cv.setTrackbarPos("Gaussian Blur", "Trackbars", p["gaussianBlurValue"])

cv.setTrackbarPos("Erode Number", "Trackbars", p["erodeNumber"])

cv.setTrackbarPos("Erode Iterations", "Trackbars", p["erodeIterations"])



while True:
    
    p['hueLow']=cv.getTrackbarPos("Hue Lower Limit","Trackbars")

    p['saturationLow']=cv.getTrackbarPos("Saturation Lower Limit","Trackbars")

    p['valueLow']=cv.getTrackbarPos("Value Lower Limit","Trackbars")

    p['hueUp']=cv.getTrackbarPos("Hue Upper Limit","Trackbars")

    p['saturationUp']=cv.getTrackbarPos("Saturation Upper Limit","Trackbars")

    p['valueUp']=cv.getTrackbarPos("Value Upper Limit","Trackbars")

    p['gaussianBlurValue']=1+2*cv.getTrackbarPos("Gaussian Blur","Trackbars")

    p['erodeNumber']=cv.getTrackbarPos("Erode Number","Trackbars")

    p['erodeIterations']=cv.getTrackbarPos("Erode Iterations","Trackbars")

    img[:,:int(p['illustrationColorWidth']/2)]=(p['hueLow'],p['saturationLow'],p['valueLow'])
    img[:,int(p['illustrationColorWidth']/2):]=(p['hueUp'],p['saturationUp'],p['valueUp'])

    img[:,:int(p['illustrationColorWidth']/2)]=cv.cvtColor(img[:,:int(p['illustrationColorWidth']/2)],cv.COLOR_HLS2BGR)
    img[:,int(p['illustrationColorWidth']/2):]=cv.cvtColor(img[:,int(p['illustrationColorWidth']/2):],cv.COLOR_HLS2BGR)


    kernal=np.ones((p['erodeNumber'],p['erodeNumber']),np.uint8)

    ret,frame=cap.read()

    frame=cv.resize(frame,(p['frameXSize'],p['frameYSize']))
    print(p['gaussianBlurValue'])
    blurredFrame=cv.GaussianBlur(frame,(p["gaussianBlurValue"],p["gaussianBlurValue"]),0)
    

    hsvFrame=cv.cvtColor(blurredFrame,cv.COLOR_BGR2HSV)

    hsvMask=cv.inRange(hsvFrame, (p['hueLow'],p['saturationLow'],p['valueLow']), (p['hueUp'],p['saturationUp'],p['valueUp']))
    
    maskErod=cv.erode(hsvMask,kernal,iterations=p['erodeIterations'])


    resultNumpy=getPlace(maskErod,p['ySegments'],p['xSegments'],p['areaFraction'])

    result=[resultNumpy[0]]
    resultNumpy=resultNumpy[1:]
    result.append(convertToXYList(resultNumpy,p['ySegments'],p['xSegments']))
    
    illustrationFrame=resultIllustrationFrame(p['ySegments'],p['xSegments'],result[1],frame.shape[0],frame.shape[1])
    
    print(result)


    #Note: there are some issues with changing the window size
    
    # cv.namedWindow("Real Frame: 1",cv.WINDOW_FREERATIO)
    # cv.namedWindow("Frame Blurred: 2",cv.WINDOW_FREERATIO)
    # cv.namedWindow("HSV  Color Mask: 3",cv.WINDOW_FREERATIO)
    # cv.namedWindow("Erosion: 4",cv.WINDOW_FREERATIO)
    # cv.namedWindow("Illustration Frame: 5",cv.WINDOW_FREERATIO)
    

    if p['showFrames']==True:


        monitorSizeWidth=1920
        monitorSizeHeight=1080

        xPixelsApart=4
        yPixelsApart=75

        if (p['frameXSize']<int(monitorSizeWidth/3) and p['frameYSize']<int(monitorSizeHeight/2)):
            
            cv.moveWindow("Real Frame: 1",0,0)
            cv.moveWindow("Frame Blurred: 2",p['frameXSize']+xPixelsApart,0)
            cv.moveWindow("HSV  Color Mask: 3",2*p['frameXSize']+2*xPixelsApart,0)

            cv.moveWindow("Erosion: 4",0,p['frameYSize']+yPixelsApart)
            cv.moveWindow("Illustration Frame: 5",p['frameXSize']+xPixelsApart,p['frameYSize']+yPixelsApart)

            #Does not work very well
            #cv.moveWindow("Trackbars",monitorSizeWidth-p['trackbarsWindowWidth'],0)


            







        if p['showSegmentation']==False:

            cv.imshow("Real Frame: 1",frame)
            cv.imshow("Frame Blurred: 2",blurredFrame)
            cv.imshow("HSV  Color Mask: 3",hsvMask)
            cv.imshow("Erosion: 4",maskErod)
            cv.imshow("Illustration Frame: 5",illustrationFrame)
            cv.imshow("Trackbars",img)

        else:

            frame=drawSegments(frame,p['ySegments'],p['xSegments'],\
            (p['bInBGRColor'],p['gInBGRColor'],p['rInBGRColor']),p['thickness'])

            blurredFrame=drawSegments(blurredFrame,p['ySegments'],p['xSegments'],\
            (p['bInBGRColor'],p['gInBGRColor'],p['rInBGRColor']),p['thickness'])

            hsvMask=drawSegments(hsvMask,p['ySegments'],p['xSegments'],\
            (255,255,255),p['thickness'])

            maskErod=drawSegments(maskErod,p['ySegments'],p['xSegments'],\
            (255,255,255),p['thickness'])

            illustrationFrame=drawSegments(illustrationFrame,p['ySegments'],p['xSegments'],\
            (255,255,255),p['thickness'])


            cv.imshow("Real Frame: 1",frame)
            cv.imshow("Frame Blurred: 2",blurredFrame)
            cv.imshow("HSV  Color Mask: 3",hsvMask)
            cv.imshow("Erosion: 4",maskErod)
            cv.imshow("Illustration Frame: 5",illustrationFrame)
            cv.imshow("Trackbars",img)

    


    if cv.waitKey(p['waitKey'])==p['keyNumber']:
        break



cap.release()
cv.destroyAllWindows()
