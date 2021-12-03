import requests
import cv2 
import numpy as np
import time
import imutils
from modular import ShapeDetector
from matplotlib.pyplot import imshow as im

url="http://192.168.1.6:8080/shot.jpg"
#url="http://192.168.43.1:8080/shot.jpg"
x1,y1=(640,480)

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
def show_webcam():
    while True:
        # Pakek ANDROID-----------------------------------------------------
        # web = requests.get(cap)
        # img_arr=np.array(bytearray(web.content),dtype=np.uint8)
        # img = cv2.imdecode(img_arr,1)
        # gray=cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
        #Pakek WEBCAM------------------------------------------------------
        ret, img_arr = cap.read()
        img_arr=cv2.resize(img_arr, (x1,y1))
        img=img_arr.copy()
        # ------------------------------------------------------------------
        gray=cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (25, 25), 1)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
        #thresh  = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        #thresh  = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        sd = ShapeDetector()
        #gray=cv2.flip(gray,1)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            try:
                M = cv2.moments(c)
                cX=int((M["m10"]/M["m00"]))
                cY = int((M["m01"] / M["m00"]))
                shape = sd.detect(c)
                if shape==None :
                      continue
            	# multiply the contour (x, y)-coordinates by the resize ratio,
            	# then draw the contours and the name of the shape on the image
                c = c.astype("float")
                c = c.astype("int")
                cv2.drawContours(img, [c], -1, (0, 255, 0), 1)
                cv2.putText(img, shape, (cX, cY), font,0.5, (255, 255, 255), 2)
            except:
                continue
        cv2.imshow('webcam', img)
        #cv2.imshow('grayscale', gray)
        cv2.imshow('threshold',thresh)
        time.sleep(0.1)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    #cap.release()
    cv2.destroyAllWindows()

def main():
    show_webcam()
if __name__ == '__main__':
    main()