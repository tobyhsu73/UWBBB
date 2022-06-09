import cv2
import numpy as np

image = cv2.imread("fl.png")

lower = np.array([22, 166, 142])
upper = np.array([62, 266, 242])

filtered = cv2.inRange(image, lower, upper)
blurred = cv2.GaussianBlur(filtered, (15, 15), 0)

# find contours in the image
cnts = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


if len(cnts) > 0:
	cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

	# compute the (rotated) bounding box around then
	# contour and then draw it		
	rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
	cv2.drawContours(image, [rect], -1, (0, 255, 0), 2)

cv2.imshow("Tracking", image)
cv2.waitKey(0)