import cv2
import numpy as np
import imutils
from imutils import contours
img = cv2.imread('2.png')
kernel = np.ones((10, 10), np.uint8)


img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      
#img=cv2.resize(img,(1920,1080))
lower_blue = np.array([25,22,184])
upper_blue = np.array([40,54,255])
mask = cv2.inRange(img, lower_blue, upper_blue)
dilation = cv2.dilate(mask, kernel, iterations=1)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
closing = cv2.GaussianBlur(closing, (5, 5), 0)
#edges = cv2.Canny(closing, 10, 20)
cnts, _ = cv2.findContours(
    closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(cnts))
if len(cnts) > 0:  # 如果檢測出了輪廓
    c = max(cnts, key=cv2.contourArea)  # 以輪廓的面積爲條件，找出最大的面積
    ((x, y), radius) = cv2.minEnclosingCircle(c)  # 找出最小的圓

    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    if radius > 5:
        cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.circle(img, center, 5, (0, 0, 255), -1)

cv2.imshow('frame',mask)
cv2.imshow('fragme',img)
