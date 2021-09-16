import camera
import os
import time
#Make sure you have two cameras on your computer
#Esc to shut down the windows and press ctr+C to stop the whole program

#These two lines will make sure that we are at the right path.
#Also, they are very useful if the code is used in other operating systems such as MAC
currentFilePath=os.path.dirname(os.path.realpath(__file__))
os.chdir(currentFilePath)

cam1=camera.Camera(0,100)
cam1.startCameraStream()
cam1.showFrames("First Camera")


cam2=camera.Camera(1,200)
cam2.startCameraStream()
cam2.showFrames("Second Camera")


#Test frames per seconds preformace
#And take image frames from the cameras
while True:
    time.sleep(0.5)
    print("Camera 1 fps: "+str(cam1.fps))
    img1=cam1.getFrame()
    time.sleep(0.5)
    print("Camera 2 fps: "+str(cam2.fps))
    img2=cam2.getFrame()
