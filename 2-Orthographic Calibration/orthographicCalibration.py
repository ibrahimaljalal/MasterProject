import cv2 as cv
import os
import numpy as np
import copy
import csv

p={
"imageWidth":800,
"imageHight":800,

"rectanglWidth":400,
"rectangleHight":400,
"rectangleStartingCoordinates":[0,0],

"circlesRadius":5,

"lineThickness":5,

"cameraType":1
}

w=p["rectanglWidth"]
h=p["rectangleHight"]
rSC=p["rectangleStartingCoordinates"]

points2=np.float32([rSC,[rSC[0]+w,rSC[1]],[rSC[0],rSC[1]+h],[rSC[0]+w,rSC[1]+h]])


currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)


cam=cv.VideoCapture(p["cameraType"])
_,img=cam.read()

#shape[0] is for hight and shape[1] is for width
def orthographicTest(img):
    #note cv.WINDOW_FREERATIO might give errors
    cv.namedWindow("Points Coordinates",cv.WINDOW_FREERATIO)


    def nothing(x):
        pass

    hight=img.shape[0]
    width=img.shape[1]
    
    #Titles on Trackbar
    p1xTitle="Point 1 (r) x:"
    p1yTitle="Point 1 (r) y:"

    p2xTitle="Point 2 (g) x:"
    p2yTitle="Point 2 (g) y:"

    p3xTitle="Point 3 (w) x:"
    p3yTitle="Point 3 (w) y:"

    p4xTitle="Point 4 (y) x:"
    p4yTitle="Point 4 (y) y:"

    #Note index starts from zero and y starts from up to buttom
    cv.createTrackbar(p1xTitle,"Points Coordinates",0,width-1,nothing)
    cv.createTrackbar(p1yTitle,"Points Coordinates",0,hight-1,nothing)

    cv.createTrackbar(p2xTitle,"Points Coordinates",width-1,width-1,nothing)
    cv.createTrackbar(p2yTitle,"Points Coordinates",0,hight-1,nothing)

    cv.createTrackbar(p3xTitle,"Points Coordinates",0,width-1,nothing)
    cv.createTrackbar(p3yTitle,"Points Coordinates",hight-1,hight-1,nothing)

    cv.createTrackbar(p4xTitle,"Points Coordinates",width-1,width-1,nothing)
    cv.createTrackbar(p4yTitle,"Points Coordinates",hight-1,hight-1,nothing)

    while True:
        #valuse will be zero if you close the trackbar window
        p1x=cv.getTrackbarPos(p1xTitle,"Points Coordinates")
        p1y=cv.getTrackbarPos(p1yTitle,"Points Coordinates")

        p2x=cv.getTrackbarPos(p2xTitle,"Points Coordinates")
        p2y=cv.getTrackbarPos(p2yTitle,"Points Coordinates")

        p3x=cv.getTrackbarPos(p3xTitle,"Points Coordinates")
        p3y=cv.getTrackbarPos(p3yTitle,"Points Coordinates")

        p4x=cv.getTrackbarPos(p4xTitle,"Points Coordinates")
        p4y=cv.getTrackbarPos(p4yTitle,"Points Coordinates")

        #point on original image
        points1=np.float32([[p1x,p1y],[p2x,p2y],[p3x,p3y],[p4x,p4y]])
        

        matrix = cv.getPerspectiveTransform(points1, points2)

        output = cv.warpPerspective(img,matrix,(p["imageWidth"],p["imageHight"]))

        
        imgC=copy.deepcopy(img)

        cv.line(imgC,(p1x,p1y),(p2x,p2y),(255,0,0),p["lineThickness"])
        cv.line(imgC,(p2x,p2y),(p4x,p4y),(255,0,0),p["lineThickness"])
        cv.line(imgC,(p4x,p4y),(p3x,p3y),(255,0,0),p["lineThickness"])
        cv.line(imgC,(p3x,p3y),(p1x,p1y),(255,0,0),p["lineThickness"])


        cv.circle(imgC,(p1x,p1y),p["circlesRadius"],(0,0,255),-1)
        cv.circle(imgC,(p2x,p2y),p["circlesRadius"],(0,255,0),-1)
        cv.circle(imgC,(p3x,p3y),p["circlesRadius"],(255,255,255),-1)
        cv.circle(imgC,(p4x,p4y),p["circlesRadius"],(0,255,255),-1)

        #cv.imshow("Real Image",img)
        cv.imshow("Real Image",imgC)

        cv.imshow("Orthographic Image",output)

        
        if cv.waitKey(50)==27:
            break
    

    #ratios
    p1xr=float(p1x/width)
    p1yr=float(p1y/hight)

    p2xr=float(p2x/width)
    p2yr=float(p2y/hight)

    p3xr=float(p3x/width)
    p3yr=float(p3y/hight)

    p4xr=float(p4x/width)
    p4yr=float(p4y/hight)

    #pixels        
    pointsCSV="{},{},{},{},{},{},{},{}".format(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y)

    #ratios
    pointsRatioCSV=[p1xr,p1yr,p2xr,p2yr,p3xr,p3yr,p4xr,p4yr]

    pointsCSV=[p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y]

    with open("points.csv","w", encoding='UTF8', newline='') as test:
        writer =csv.writer(test)
        #writer.writerow(pointsCSV)
        writer.writerow(pointsRatioCSV)
       
    cv.destroyAllWindows()
    
   
if __name__=="__main__":
    orthographicTest(img)

    
