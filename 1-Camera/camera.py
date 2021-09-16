import cv2 as cv
from threading import Thread
import numpy as np
import time

class Camera:
    def __init__(self,cameraType,waitKey,defaultResolution=True,
    widthResolution=640,hightResolution=480,defaultSize=True,widthSize=500,hightSize=500,keyNumber=27):

        self.cameraType=cameraType
        self.waitKey=waitKey
        self.keyNumber=keyNumber
        self.defaultSize=defaultSize
        self.widthSize=widthSize
        self.hightSize=hightSize
        self.fps=0

        if isinstance(cameraType,str)!=True:  
            while True:
                self.cam=cv.VideoCapture(self.cameraType)
                if (self.cam.isOpened()==True):
                    break

                if (self.cameraType>=0):
                    self.cameraType=self.cameraType-1
                if (self.cameraType<0):
                    self.cameraType=self.cameraType+1

        
        if defaultResolution!=True:
            self.cam.set(3,widthResolution)
            self.cam.set(4,hightResolution)


    def __start(self):
        while True:
                self.__timeStamp=time.time()                                                        
                _,self.img=self.cam.read()
                if self.defaultSize!=True:
                    self.img=cv.resize(self.img,(self.widthSize,self.hightSize))
                cv.waitKey(self.waitKey)
                self.__dt=time.time()-self.__timeStamp
                self.fps=1.0/self.__dt
                

    def startCameraStream(self):      

        self.__camThread=Thread(target=self.__start,daemon=True)
              
        self.__camThread.start()
    

    def getFrame(self):
        while True:
            try:                
                return self.img
            except AttributeError:
                pass
                    

    def __show(self,frameTitle):
        while True:
            try:
                cv.imshow(frameTitle,self.img)
                if cv.waitKey(self.waitKey)==self.keyNumber:
                    break
            except:
                pass    

    def showFrames(self,frameTitle=""):

        self.__showFramesThread=Thread(target= self.__show,args=(frameTitle,),daemon=True)
        self.__showFramesThread.start()
            

    




