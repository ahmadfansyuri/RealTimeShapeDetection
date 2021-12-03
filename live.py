import requests
import cv2 
import numpy as np
import time
url="http://192.168.100.4:8080/shot.jpg"
#url="http://192.168.43.1:8080/shot.jpg"
x,y=(640,480)
def threshold(img):
    parse=np.array(img)
    parse=parse.reshape(6400)
    if parse.sum()/6400 < 100:
        return "1" #Hitam
    return "0" #Putih

def show_webcam():
    x,y=(640,480)
    crops=[]
    garis=cv2.imread("garis.jpg")
    garis=cv2.cvtColor(garis,cv2.COLOR_BGR2GRAY)
    back=cv2.imread("background.jpg")
    while True:
        hasil=""
        web = requests.get(url)
        img_arr=np.array(bytearray(web.content),dtype=np.uint8)
        img = cv2.imdecode(img_arr,1)
        gray=cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
        gray=cv2.flip(gray,1)
        for i in range(0,x,80):
            crops.append(gray[240:320,i:i+80].copy())
        for foto in range(0,8):
            hasil+=threshold(crops[foto])+" "
            try:
                sample=np.concatenate((sample,crops[foto]),axis=1)
                sample=np.concatenate((sample,garis),axis=1)
            except:
                sample=crops[foto]
                sample=np.concatenate((sample,garis),axis=1)
        sensor=sample[:,:-10].copy()
        text=cv2.putText(back.copy(),hasil,color=(0,0,0),org=(10,40),fontScale=1,fontFace=cv2.FONT_HERSHEY_COMPLEX)
        cv2.imshow("Mulai",text)
        cv2.imshow('webcam', img)
        cv2.imshow('grayscale', gray)
        cv2.imshow('sensor',sensor)
        time.sleep(0.1)
        crops=[]
        sample=[]
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cap.release()
    cv2.destroyAllWindows()

def main():
    show_webcam()
if __name__ == '__main__':
    main()