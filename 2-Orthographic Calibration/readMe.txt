Description:
----------------------------------------------------------------------
This code will help us in transforming an image frame into an orthographic view. In order to do that we should manually put 4 points on the corners of a rectangular surface from our image coming from the camera then the function will output points.csv file. this output will be used from another function.
Just like most codes, the p dictionary variable will give the user all of the necessary control over the program.
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
This code should be used only once for calibrating the camera and should not be used agin unless the camera orientation has changed.
----------------------------------------------------------------------


Parameters/Specifications:
----------------------------------------------------------------------
imageWidth (int): the frame output width in pixels
imageHight (int): the frame output hight in pixels
rectanglWidth (int): the width of the rectangle in pixels that will be displayed in the image (frame output)
rectanglHight (int): the hight of the rectangle in pixels that will be displayed in the image (frame output)
rectangleStartingCoordinates (int list): the rectangle starting point in x and y coordinates (upper left corner) with respect to the image (frame output)
circlesRadius (int): the radius of the circles that will be displayed to illustrate the corners of the rectangle
lineThickness (int): the blue line thickness connecting the points
cameraType (int): the from your computer (usually it is either 0 or 1)
----------------------------------------------------------------------