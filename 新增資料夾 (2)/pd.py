
import cv2
import numpy as np

img = cv2.imread('ww.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
      
img=cv2.resize(img,(1920,1080))
lower_blue = np.array([18,141,99])
upper_blue = np.array([32,198,177])
mask = cv2.inRange(img, lower_blue, upper_blue)
blurred = cv2.GaussianBlur(mask, (15, 15), 0)
# find contours in the image
(x, cnts, z) = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


if len(cnts) > 0:
	cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

	# compute the (rotated) bounding box around then
	# contour and then draw it		
	rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
	cv2.drawContours(image, [rect], -1, (0, 255, 0), 2)

cv2.imshow("Tracking", image)
cv2.waitKey(0)
cv2.imshow('frame',mask)

