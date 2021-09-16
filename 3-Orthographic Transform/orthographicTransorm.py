import cv2 as cv
import csv
import numpy as np
import os

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

p={
"imageWidth":800,
"imageHight":800,
 
"rectanglWidth":700,
"rectanglehight":400,
"rectangleStartingCoordinates":[0,0],

"pointsRatio":[0,0,0.5,0,0,0.5,0.5,0.5],
}

points1Ratio=None

def readFromCSV(csvFile="points.csv"):
    global points1Ratio
    with open(csvFile,"r") as file:
            csv_reader=csv.reader(file)

            
            for line in csv_reader:
                csvFile=line

            points1Ratio=np.float32([[csvFile[0],csvFile[1]],[csvFile[2],csvFile[3]],[csvFile[4],csvFile[5]],[csvFile[6],csvFile[7]]])

def transform(img,points=p["pointsRatio"]):
    readFromCSV()
    global points1Ratio

    hight=img.shape[0]
    width=img.shape[1]

    if points1Ratio is None:
        points1Ratio=points

    w=p["rectanglWidth"]
    h=p["rectanglehight"]
    rSC=p["rectangleStartingCoordinates"]
    points2=np.float32([rSC,[rSC[0]+w,rSC[1]],[rSC[0],rSC[1]+h],[rSC[0]+w,rSC[1]+h]])

    pxInt=[]
    pyInt=[]
    
    for i in range(len(points1Ratio)):
        pxInt.append(int(width*points1Ratio[i][0]))
        pyInt.append(int(hight*points1Ratio[i][1]))

    points1=np.float32([[pxInt[0],pyInt[0]],[pxInt[1],pyInt[1]],[pxInt[2],pyInt[2]],[pxInt[3],pyInt[3]]])  
    matrix = cv.getPerspectiveTransform(points1, points2)
    output = cv.warpPerspective(img,matrix,(p["imageWidth"],p["imageHight"]))

    return output

