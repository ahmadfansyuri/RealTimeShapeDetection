"# RealTimeShapeDetection" 

This code was created as one of the assignments for an introduction to embedded systems course. This code aims to calculate the area value of an object with the input being video (Internal camera/External camera).

In this repository there are two files, the first is the main code and the second is the modular code which contains the "ShapeDetector" library code. In the "edge.py" file the code can be used to retrieve data from a laptop camera or an external camera (from a smartphone). After the image is obtained, the image will be changed to grayscale and then using a gaussian blur filter and using a manually filled threshold (with values following environmental and camera conditions). Then the output value of the thresh variable will use the cv2.findContours method to calculate the contour line or contour of a function, two variables are curves where the function has a constant value.

The explanation of each attribute can be read here:
