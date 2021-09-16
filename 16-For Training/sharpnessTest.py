import cv2 as cv

#parameters
#########################################
p={

'grayImage': False,

'cameraNumber': 1,
'waitKey': 50,
'keyNumber': 27,

'defaultResolution': True,
'cameraResolutionWidth': 320, 
'cameraResolutionHight': 240,

'defaultSize':True,
'frameXSize': 1000,
'frameYSize': 600,
}
#########################################


#This function will catch the camera even if the camera number is wrong
#############################################################
def setCamera(cameaNumber=p['cameraNumber']):
    while True:

            cap=cv.VideoCapture(cameaNumber)
            if (cap.isOpened()==True):
                return cap

            if (cap.isOpened()==False and cameaNumber>=0):
                cameaNumber=cameaNumber-1
            if (cap.isOpened()==False and p['cameraNumber']<0):
                cameaNumber=cameaNumber+1

#############################################################

#############################################################
def setResolution(cap):
    if p['defaultResolution']==False:
        cap.set(3,p['cameraResolutionWidth'])
        cap.set(4,p['cameraResolutionHight'])
        return cap

    return cap

#############################################################

#############################################################
def setSize(frame):
    if p['defaultSize']==False:
        frame=cv.resize(frame,(p['frameXSize'],p['frameYSize']))
        return frame
    
    return frame

#############################################################

cap=setCamera()
cap=setResolution(cap)

while True:
    _,img=cap.read()
    img=setSize(img)
    if p['grayImage']==True:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    #if laplacian_var is lower than it is more blurry
    #https://www.youtube.com/watch?v=5YP7OoMhXbM&t=225s
    laplacian_var=cv.Laplacian(img,cv.CV_64F).var()
    #####################################

    #https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
    laplacian_var="{:.2f}".format(laplacian_var)
    

    #https://www.youtube.com/watch?v=rRSyg9kYfcU
    #I have added the details
    font=cv.FONT_HERSHEY_SIMPLEX
    #cv.putText(img,"blurlensess is: "+str(laplacian_var),(int(img.shape[2]/2),int(img.shape[1]/2)),font,1,(255,0,0),2,cv.LINE_AA)

    cv.putText(img,"Sharpness Value is: "+str(laplacian_var),(int(img.shape[1]/20),int(img.shape[0]/15)),font,1,(255,0,0),2,cv.LINE_AA)
    #####################################

    cv.imshow("Sharpness Test",img)

    if cv.waitKey(p['waitKey'])==p['keyNumber']:
        break