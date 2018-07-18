#Import Numpy and cv2 libraries
import numpy as np
import cv2 as cv


# Create the haar cascade for both face and eye recognition
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

# Create two variable one that will contain the image to analyze and the other to convert the image in grayscale
img = cv.imread('test2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# This function is used to recognize faces
faces = face_cascade.detectMultiScale(gray, 1.9, 5)

# Create a rectangle on faces and eyes
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    gray_main = gray[y:y+h, x:x+w]
    color_main = img[y:y+h, x:x+w]
    
    # This function is used to recognize the eyes on the image
    eyes = eye_cascade.detectMultiScale(gray_main)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(color_main,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
#cv.imshow('gray', gray)

#Finally you use the function to show the image the algorithm analysed
cv.imshow('img',img)	
cv.waitKey(0)
cv.destroyAllWindows()