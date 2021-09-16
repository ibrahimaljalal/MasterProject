import cv2 as cv
from datetime import datetime
import numpy as np
from enum import Enum
import os
import time
import re
from threading import Thread


#parameters
#########################################
p={

'object':'Remote',

'addPositiveAndNegative':False,

#time in seconds
'timeBetweenImages': 2,

'grayImage': False,

#smaller valuse means more blurlensess
'sharpness':50,

'saveFromCamera':True,

'folderName':'Object_',

'numberOfImages':20,

'imageType':'png',

'cameraNumber': 1,
'waitKey': 50,
'keyNumber': 27,


#Make sure to make the width and hight in right proportion
#The least for my camera seems to be 160*120 
#(if you lower it you will get an error)
'defaultResolution': True,
'cameraResolutionWidth': 320, 
'cameraResolutionHight': 240,

'defaultSize':True,
'frameXSize': 1000,
'frameYSize': 600,


'showFrames': True

}

#########################################


#camera Class
#########################################
class camera:
    #waitKey means that it will wait in ms
    def __init__(self,cap,waitKey=1,defaultSize=p['defaultSize'],
    frameXSize=p['frameXSize'],frameYSize=p['frameYSize']):

        self.defaultSize=defaultSize
        self.frameXSize=frameXSize
        self.frameYSize=frameYSize

        self.__camThread=Thread(target=self.__startCamera,args=(cap,waitKey),daemon=True)
              
        self.__camThread.start()

        self.waitKey=waitKey

    

    def __startCamera(self,cap,waitKey):
        while True:
            if self.defaultSize==True:
                _,self.img=cap.read()
                cv.waitKey(waitKey)
            else:
                _,self.imgBefore=cap.read()
                self.img=cv.resize(self.imgBefore,(self.frameXSize,self.frameYSize))

    def getFrame(self):
        while True:
            try:        
                return self.img
            except:
                pass         
                    

    def __show(self,frameTitle,waitShow,keyNumber):
        while True:
            try:
                cv.imshow(frameTitle,self.img)
                if cv.waitKey(waitShow)==keyNumber:
                    break
            except:
                pass    

    def showFrames(self,frameTitle="",waitShow=p['waitKey'],keyNumber=p['keyNumber']):
        
        self.__showFramesThread=Thread(target= self.__show,args=(frameTitle,waitShow,keyNumber),daemon=False)
        self.__showFramesThread.start()
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


#############################################################
def cheakForDuplicats(listOfFolders):
    for i in listOfFolders:
        if i !=None:
            return True
    return False

#############################################################



#############################################################
def saveImages(cam,timeBetweenImages=p['timeBetweenImages'],grayImage=p['grayImage'],
sharpness=p['sharpness'],waitKey=p['waitKey'],keyNumber=p['keyNumber'],
showFrames=False,numberOfImages=p['numberOfImages'],
type=p['imageType'],path=os.path.dirname(os.path.realpath(__file__))):
    
    if showFrames==True:
        cam.showFrames("Frame_1",waitKey,keyNumber)

    counter=1

    while counter<=numberOfImages:
        img = cam.getFrame()

        if grayImage==True:
            img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        
        #https://www.youtube.com/watch?v=5YP7OoMhXbM&t=225s
        laplacian_var=cv.Laplacian(img,cv.CV_64F).var()
        #if laplacian_var is lower than it is more blurry

        if laplacian_var>sharpness:
            cv.imwrite(os.path.join(path,str(counter)+'.'+type),img)
            time.sleep(timeBetweenImages)
            counter=counter+1
#############################################################


#############################################################
def takeImages(name,cam):

    currentFilePath=os.path.dirname(os.path.realpath(__file__))

    os.chdir(currentFilePath)

    folderName=p['folderName']
    
    if p['saveFromCamera']==True:

        counter=1

        pattern=r''+str(folderName)+str(counter)+str('.*')
        listOfPatterns=[]
        for i in list(map(re.match,tuple([pattern]*len(os.listdir())),tuple(os.listdir()))):
    
            if type(i) !=type(None):
                listOfPatterns.append(i.group())
            else:
                listOfPatterns.append(i)

        
        while cheakForDuplicats(listOfPatterns):
            counter=counter+1

            pattern=r''+str(folderName)+str(counter)+str('.*')
            listOfPatterns=[]
            for i in list(map(re.match,tuple([pattern]*len(os.listdir())),tuple(os.listdir()))):
    
                if type(i) !=type(None):
                    listOfPatterns.append(i.group())
                else:
                    listOfPatterns.append(i)

            
            
        if p['addPositiveAndNegative']==True:
            print("\n")
            print("Collacting "+str(p['numberOfImages'])+" images for "+str(name)+":")
            print("-------------------------------------------")
            os.makedirs(os.path.join(os.getcwd(),folderName+str(counter)+'_'+str(name),'p'))
            input("Press enter to start collecting the positive data: ")
            saveImages(cam,path=os.path.join(os.getcwd(),folderName+str(counter)+'_'+str(name),'p'))
            os.makedirs(os.path.join(os.getcwd(),folderName+str(counter)+'_'+str(name),'n'))
            input("Press enter to start collecting the negative data: ")
            saveImages(cam,path=os.path.join(os.getcwd(),folderName+str(counter)+'_'+str(name),'n'))
            print("Done!")
            print("-------------------------------------------")
            print("\n")
        else:
            print("\n")
            print("Collacting "+str(p['numberOfImages'])+" images for "+str(name)+":")
            print("-------------------------------------------")
            os.makedirs(os.path.join(os.getcwd(),folderName+str(counter)+'_'+str(name)))
            input("Press enter to start collecting the  data: ")
            saveImages(cam,path=os.path.join(os.getcwd(),folderName+str(counter)+'_'+str(name)))
            print("Done!")
            print("-------------------------------------------")
            print("\n")

#############################################################


if __name__=="__main__":
    cap=setCamera()
    cap=setResolution(cap)
    
    cam=camera(cap)


    if p['showFrames']==True:
        cam.showFrames("Images for Training")

    takeImages(p['object'],cam)

    
    





