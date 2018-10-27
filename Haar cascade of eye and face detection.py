import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cx=int(x+(w/2))
        cy=int(y+(h/2))
        if(w>h):
            cv2.circle(img,(cx,cy),(int(w/2)),(0,0,255),2)
        else:
            cv2.circle(img,(cx,cy),(int(h/2)),(0,0,255),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        
        eyes=eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(50,33,100),2)
            
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xFF
    if k ==27:
        break
cap.release()
cv2.destroyAllWindows()
    
    
