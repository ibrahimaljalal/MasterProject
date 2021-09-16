Description:
----------------------------------------------------------------------
This code will enable us to take images from multiple cameras at the same time (by using multithreding) in our case we will take from two cameras. Also, we could easily control all of the necessary specifications such as the image resolution, size and delay from the Camera contractor class.
Just like most codes, The staring point is at main.py file.
Just like most codes, the results/outputs are in the Results directory
----------------------------------------------------------------------


Software:
----------------------------------------------------------------------
Operating System: tested on Windows but should work on MAC and Linux
Programming language(s): Python 3.8.8
Libraries: opencv (cv2) (version 4.5.2 )
----------------------------------------------------------------------


Instructions/Notes:
----------------------------------------------------------------------
pip install opencv-python
pip install opencv-contrib-python
Notes:
The code in main.py will not work if you don't have two cameras or more
Press Esc to shut down the windows and press ctr+C to stop the whole program
----------------------------------------------------------------------


Parameters/Specifications (Camera constructor):
----------------------------------------------------------------------
cameraType (int): the camera you want to read from (if you have three cameras on your computer then type 0,1, and 2 at the class constructors for three objects made from the Camera class)
waitKey (int): time in milliseconds between the frames (if you lower it you will increase the frames per seconds of the camera object)
defaultResolution (bool): if it is True then the width and hight resolution parameters after it will not change the resolution of the camera object.
widthResolution (int): Number of pixels in the width of the frame
hightResolution (int): Number of pixels in the hight of the frame
defaultSize (int): if it is True then the width and hight sizes parameters after it will not change the size of the frame. Note that this is not exactly the same as the resolution because you cloud have a low resolution image but with a lot of pixels (Scaled frame)
widthSize (int): Number of pixels in the width of the frame
hightSize (int): Number of pixels in the width of the frame
keyNumber (int): The key on our keyboard that will close the window. Note that it is ascii number corresponding to the key pressed (we usually choose 27 to represent the Esc key)
----------------------------------------------------------------------