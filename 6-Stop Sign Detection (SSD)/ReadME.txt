Description:
----------------------------------------------------------------------
This file will simply search for a stop sign.
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
main.py depends on three files so make sure you do not delete them. they are:
1-stopSignAvailable.py
2-ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
3-frozen_inference_graph.pb
4-Lables.txt
make sure you choose the right camera number
----------------------------------------------------------------------


Parameters/Specifications:
----------------------------------------------------------------------
objectsLabels: you can choose the objects you want to detect from the Lables.txt file. the objects are labeled according to the line number they are on the file.
objectDetectedFractionalArea: the object detected area over the whole frame area. Any object below this limit will not be detected,
accuracy: the accuracy or (certainty) of the result
showFrames: if it is True it will show the frames otherwise it will output True or False
The below four parameters are for illustrational purposes:
-------------------
rectangleColor: the color of the rectangle that will be over the detected object
fontScale: the font of the name of the detected object
fontThickness: the thickness of font for the object
fontColor: the color of the font
----------------------------------------------------------------------
