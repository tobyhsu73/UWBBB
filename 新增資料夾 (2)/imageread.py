import cv2
import numpy as np
import imutils
from imutils import contours
from collections import deque
import givedataul
import time
i=0
n=1
pts = deque()

kernel = np.ones((5, 5), np.uint8)
data=givedataul.getdata()
uxl=data
data=givedataul.getdata()
uyl=data
data=givedataul.getdata()
xcl=data
data=givedataul.getdata()
ycl=data
data=givedataul.getdata()
uxt=data
data=givedataul.getdata()
uyt=data
print(len(uyt))
print(len(uyl))
'''
for a in range(60):
    ret, frame = cap.read()
    print(a)
    '''

    
img1=cv2.imread('5.png')
img1=cv2.resize(img1,(1920,1080))
img1 = img1[300:1000, 50:1920]
zerox=1880
zeroy=570
xc=21
yc=20
cv2.line(img1, (zerox*xc,zeroy), (zerox-90*xc,zeroy), (255, 255,255), 2,)
cv2.line(img1, (zerox*xc,zeroy-10*yc), (zerox-90*xc,zeroy-10*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox*xc,zeroy-20*yc), (zerox-90*xc,zeroy-20*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox*xc,zeroy), (zerox*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-10*xc,zeroy), (zerox-10*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-20*xc,zeroy), (zerox-20*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-30*xc,zeroy), (zerox-30*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-40*xc,zeroy), (zerox-40*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-50*xc,zeroy), (zerox-50*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-60*xc,zeroy), (zerox-60*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-70*xc,zeroy), (zerox-70*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-80*xc,zeroy), (zerox-80*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.line(img1, (zerox-90*xc,zeroy), (zerox-90*xc,zeroy-24*yc), (255, 255,255), 2,)
cv2.circle(img1, (zerox-xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-xc,zeroy-12*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-10*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-20*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-30*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-40*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-50*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-60*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-70*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-80*xc,zeroy), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-10*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-20*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-40*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-50*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-60*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-70*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-80*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-90*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.circle(img1, (zerox-30*xc,zeroy-24*yc), 8, (0,255,255), -1)
cv2.putText(img1, '0m', (1820, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '10m', (1620, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '20m', (1420, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '30m', (1220, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '40m', (1020, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '50m', (820, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '60m', (600, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '70m', (390, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '80m', (180, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '0m', (1820, 600), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '10m', (1790, 400), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(img1, '20m', (1790, 200), cv2.FONT_HERSHEY_COMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
#cv2.putText(img1, '紅點:遙控船影像位置  紅線:遙控船歷史路徑 藍點:遙控船UWB定位位置 藍線:遙控船UWB歷史路徑 黃點:UWB anchor 架設位置', (1420, 700),  cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2, cv2.LINE_AA)
#xxx=int(1800-uy*18.8)
#yyy=int(570-20.7*ux)
'''    
for i in range(len(xcl)):
    if i==0:
        continue
    try:
        cv2.line(img1, (xcl[i], ycl[i]), (xcl[i-1], ycl[i-1]), (0, 0, 255), 3)
    except:
        continue
'''
for i in range(len(uxl)):
    if i<20:
        continue
    try:
        if i>=4305:
        
            cv2.line(img1, (int(1955-uyt[i]*21.4) , int(534-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(534-22.04*uxt[i])), (255, 0,0), 3)
        elif i>=4005:
            
            cv2.line(img1, (int(1955-uyt[i]*21.4) , int(534-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(534-22.04*uxt[i])), (255, 0,0), 3)
        elif i>=2225:
            
            cv2.line(img1, (int(1955-uyt[i]*21.4) , int(534-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(534-22.04*uxt[i])), (255, 0,0), 3)
        elif i>1800:
            cv2.line(img1, (int(1955-uyt[i]*21.4) , int(520-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(520-22.04*uxt[i])), (255, 0,0), 3)
        elif i>1000:
            cv2.line(img1, (int(1955-uyt[i]*21.4) , int(520-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(520-22.04*uxt[i])), (255, 0,0), 3)
        elif i>780:
            cv2.line(img1, (int(1955-uyt[i]*21.1) , int(518-22.04*uxt[i])), (int(1955-uyt[i]*21.1), int(518-22.04*uxt[i])), (255, 0,0), 3)
        elif i>586:
            cv2.line(img1, (int(1955-uyt[i]*21.15) , int(512-22.04*uxt[i])), (int(1955-uyt[i]*21.15), int(512-22.04*uxt[i])), (255, 0,0), 3)
        else:
            cv2.line(img1, (int(1955-uyt[i]*21.4) , int(515-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(515-22.04*uxt[i])), (255, 0,0), 3) 
    
    except:
        continue        
#cv2.line(img1, (int(1800-uyt[i]*18.8) , int(570-20.7*uxt[i])), (int(1800-uyt[i-1]*18.8), int(570-20.7*uxt[i-1])), (255, 0,0), 3) 
cv2.imshow('fragme',img1)

