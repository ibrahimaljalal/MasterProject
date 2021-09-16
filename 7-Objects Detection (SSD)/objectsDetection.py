import cv2 as cv
import os
import copy

#Note make sure that showFrames is False when you want to apply the code
# 1 = person, 2 = bicycle, 3 = car, 4 = motorbike, 6 = bus, 8 = truck, and 10 = traffic light

p={   
"objectsLabels":[1,2,3,4,6,8,10],

#If lower it will also detect smaller objects
"objectDetectedFractionalArea":0.0,

#float from 0 to 1
"accuracy":0.5,


"showFrames":True,


#Not important (only for illustration)
########################################
"rectangleColor":(255,0,0),
#floate
"fontScale":2,
"fontThickness":2,
"fontColor":(255,0,0),
########################################
}

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv.dnn_DetectionModel(frozen_model,config_file)

classLabels = []
file_name = 'Lables.txt'

with open(file_name,"rt") as fpt:
    classLabels=fpt.read().rstrip("\n").split('\n')

#Most resources use these numbers (no need to know what they exactly mean)
##########################################
model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)
##########################################

def objectsAvailable(img):
    thereIsAnObject=False
    hight=img.shape[0]
    width=img.shape[1]

    imageARea=hight*width

    font=cv.FONT_HERSHEY_PLAIN
    #The output type is either a numpy array (list inside a list) or an empty tuple
    #bbox is a lists of objects inside a list 
    #every list has the coordinates of the upper left corner of a rectingle then the width and hight
    ClassIndex, confidece,bbox=model.detect(img,confThreshold=p["accuracy"])

    if isinstance(ClassIndex,tuple):
        if p["showFrames"]==True:
            return img
        else:    
            return False

    outimg=copy.deepcopy(img)
    for ClassInd, conf, box in zip(ClassIndex.flatten(),confidece.flatten(),bbox):
        objectArea=box[2]*box[3]
        objectAreaFraction=objectArea/imageARea
             
    
        if (ClassInd in p["objectsLabels"]) and conf>p["accuracy"] and objectAreaFraction>p["objectDetectedFractionalArea"]:
            thereIsAnObject=True
            if p["showFrames"]==True:  
                cv.rectangle(outimg,box,(255,0,0),2)
                cv.putText(outimg,"{}, {:.2f}".format(classLabels[ClassInd-1],conf),(box[0],box[1]-10),font,fontScale=p["fontScale"],color=p["fontColor"],thickness=p["fontThickness"])
        
    if p["showFrames"]==True:    
        return outimg
    else:
        return thereIsAnObject




        


