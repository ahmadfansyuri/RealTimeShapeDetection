"# RealTimeShapeDetection" 

This code was created as one of the assignments for an introduction to embedded systems course. This code aims to calculate the area value of an object with the input being video (Internal camera/External camera).

In this repository there are two files, the first is the main code and the second is the modular code which contains the "ShapeDetector" library code. In the "edge.py" file the code can be used to retrieve data from a laptop camera or an external camera (from a smartphone). After the image is obtained, the image will be changed to grayscale and then using a gaussian blur filter and using a manually filled threshold (with values following environmental and camera conditions). Then the output value of the thresh variable will use the cv2.findContours method to calculate the contour line or contour of a function, two variables are curves where the function has a constant value.

Then the modular file has a function to do calculation from the image that retrieve from the camera. 

![Flow Chart](https://github.com/ahmadfansyuri/RealTimeShapeDetection/blob/main/Flowchart_Cut.png?raw=true)

The explanation of each attribute can be read here:

cv2.threshold    : https://www.geeksforgeeks.org/find-and-draw-contours-using-opencv-python/#:~:text=We%20see%20that%20there%20are,the%20contours%20in%20the%20image. <br/>
cv2.GaussianBlur : https://www.tutorialspoint.com/opencv/opencv_gaussian_blur.htm<br/>
cv2.findContours : https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html<br/>


Iam open for consctructive ideas, suggestions, and critism.
