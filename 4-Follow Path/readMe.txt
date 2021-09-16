Description:
----------------------------------------------------------------------
This code will take an image which contains a colored path and will estimate the angle in degrees we should rotate in order to follow the path.
Just like most codes, The staring point is at main.py file.
Just like most codes, the p dictionary variable will give the user all of the necessary control over the program.
Just like most codes, the results/outputs are in the Results directory.
The Illustrations folder will help the user with the code.
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
The explanation of this code might not be very clear but it should be understood after the whole project presentation
----------------------------------------------------------------------


Parameters/Specifications:
----------------------------------------------------------------------
baseFraction (float): The fraction the frame will be used from bellow in order to estimate the staring point of a line the the x axis
histogramFraction (float): If the number of white pixels in any vertical axes over the frame hight (vertical axis) are lower then histogramFraction then this axes x coordinate will not be computed in the average to estimate the one of the two vertical lines line.
hsvLower (int list): The lower HSV color range allowed to detect a pixel (Refer to the Illustrations folder)
hsvUpper (int list): The upper HSV color range allowed to detect a pixel (Refer to the Illustrations folder)
kernelSize (int): the square matrix size that will filter the image (Refer to the Illustrations folder)
kernelFactor (int): the value that will be multiplied with the square matrix composed of ones
dilate (int): This will dilate the frame (make the white pixels more)
erode (int): This will erode the frame (make the white pixels lower)
applyErode (bool): if it is true then only erosion will be applied and vice versa
showFrames (bool): this will show the frames for illustrational proposes
PrintAngle (bool): the angle will be printed in the terminal
----------------------------------------------------------------------