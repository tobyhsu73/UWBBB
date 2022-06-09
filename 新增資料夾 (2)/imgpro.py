import cv2
import numpy as np
import imutils
from imutils import contours
from collections import deque
import givedataul
import time
kernel = np.ones((5, 5), np.uint8)
img1=cv2.imread('w4.png')
#img1 = img1[300:1000, 0:1920]
img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
lower_blue = np.array([25,22,214])
upper_blue = np.array([40,54,255])
#lower_blue = np.array([25,33,221])
#upper_blue = np.array([37,94,255])
mask = cv2.inRange(img, lower_blue, upper_blue)

dilation = cv2.dilate(mask, kernel, iterations=1)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
cv2.imshow('dfffsff',closing)
closing = cv2.GaussianBlur(closing, (5, 5), 0)
cv2.imshow('dfffff',closing)
#edges = cv2.Canny(closing, 10, 20)
cnts, _ = cv2.findContours(
    closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if len(cnts) > 0:  # 如果檢測出了輪廓
    '''
    for i in range(len(cnts)):
        area = cv2.contourArea(cnts[i])
        print(area)
    '''   

    c = max(cnts, key=cv2.contourArea)  # 以輪廓的面積爲條件，找出最大的面積
    ((x, y), radius) = cv2.minEnclosingCircle(c)  # 找出最小的圓

    M = cv2.moments(c)
    #print(x)
    #print(y)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))       
    if radius > 1:
        cv2.circle(img1, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.circle(img1, center, 5, (0, 0, 255), -1)
   
cv2.imshow('ff',img1)
cv2.imshow('dff',img)
