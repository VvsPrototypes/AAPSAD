import cv2
import numpy as np
import sys
import time
import os

facePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(facePath)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
sF = 1.05


ret, frame = cap.read()
img = frame
time.sleep(2)
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor= sF,
	minNeighbors=8,
	minSize=(55, 55),
	flags=cv2.CASCADE_SCALE_IMAGE
)
c = cv2.waitKey(7) % 0x100
cap.release() 
if (len(faces)):
  	cv2.imwrite(filename = 'emo.jpg', img=frame)
	print('opening API')
	os.system('python emotion.py')
	time.sleep(10)
