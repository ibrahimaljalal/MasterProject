Description:
----------------------------------------------------------------------
This code will either use points.csv file to transform an image into an orthographic view or we could use the points argument in the transform function (Note that if points.csv file is present then the points argument will not have any effect).
Just like most codes, The staring point is at main.py file.
Just like most codes, the p dictionary variable will give the user all of the necessary control over the program.
Just like most codes, the results/outputs are in the Results directory.
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
Note: this code could work independently from points.csv file. if you want to relate the code in 2-OrthographicCalibration to this code then simply copy the values in points.csv file in 2-OrthographicCalibration directory and past them in points.csv file in 3-OrthographicTransform directory.
----------------------------------------------------------------------


Parameters/Specifications:
----------------------------------------------------------------------
imageWidth (int): the frame output width in pixels
imageHight (int): the frame output hight in pixels
rectanglWidth (int): the width of the rectangle in pixels that will be displayed in the image (frame output)
rectanglHight (int): the hight of the rectangle in pixels that will be displayed in the image (frame output)
rectangleStartingCoordinates (int list): the rectangle starting point in x and y coordinates (upper left corner) with respect to the image (frame output)
pointsRatio (float list): these are the four points x and y coordinates ratios taken from points.csv file
----------------------------------------------------------------------