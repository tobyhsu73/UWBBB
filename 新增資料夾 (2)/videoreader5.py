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
cap = cv2.VideoCapture('5.mp4')
kernel = np.ones((5, 5), np.uint8)
data=givedataul.getdata()
ux1=data['x']
uy1=data['y']
t1=data['t']
uxl=[]
uyl=[]
xcl=[]
ycl=[]
uxt=[]
uyt=[]
print(data)

for a in range(11):
    ret, frame = cap.read()
    print(a)
    
while(True):
    
    i=i+1
    print(i)
    for a in range(2):
        ret, frame = cap.read()
    
    if i==3374:
        f=open('423'+'.txt','a')
        uxl=str(uxl)
        uyl=str(uyl)
        xcl=str(xcl)
        ycl=str(ycl)
        uxt=str(uxt)
        uyt=str(uyt)
        f.write(uxl+'\n')
        f.write(uyl+'\n')
        f.write(xcl+'\n')
        f.write(ycl+'\n')
        f.write(uxt+'\n')
        f.write(uyt+'\n')
    
    ret, frame = cap.read()
    img1=cv2.resize(frame,(1920,1080))
    img1 = img1[300:1000, 0:1920]
    (h, w, d) = img1.shape      # 讀取圖片大小

    img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
          

    lower_blue = np.array([25,22,214])
    upper_blue = np.array([40,54,255])
    #lower_blue = np.array([25,33,221])
    #upper_blue = np.array([37,94,255])
    mask = cv2.inRange(img, lower_blue, upper_blue)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
    closing = cv2.GaussianBlur(closing, (5, 5), 0)
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
     
        if i==1:
            d=3
            ox=x
            oy=y
            
        else:
            
            d=((x-ox)**2+(y-oy)**2)**0.5
            
        if radius > 1 and d<40:
            cv2.circle(img1, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(img1, center, 5, (0, 0, 255), -1)
            xcl.append(int(x))
            ycl.append(int(y))
            ox=x
            oy=y
           
    if i==n:   
        data=givedataul.getdata()
        ux=data['x']
        uy=data['y']
        t=data['t']
        timer=t-t1
        
        timer=round(timer,1)*10        
        n=int(timer)+1
   

    zerox=1880
    zeroy=570
    xc=21
    yc=20
    cv2.line(img1, (zerox*xc,zeroy), (zerox*xc,zeroy-24*yc), (255, 255,255), 2,)
    cv2.line(img1, (zerox*xc,zeroy), (zerox-90*xc,zeroy), (255, 255,255), 2,)
    cv2.line(img1, (zerox*xc,zeroy-10*yc), (zerox-90*xc,zeroy-10*yc), (255, 255,255), 2,)
    cv2.line(img1, (zerox*xc,zeroy-20*yc), (zerox-90*xc,zeroy-20*yc), (255, 255,255), 2,)
    cv2.line(img1, (zerox-xc,zeroy), (zerox-xc,zeroy-24*yc), (255, 255,255), 2,)
    
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
    cv2.circle(img1, (1739,555), 3, (0,255,255), -1)
    cv2.circle(img1, (1710,65), 3, (0,255,255), -1)
    cv2.circle(img1, (1513,65), 3, (0,255,255), -1)
   # cv2.circle(img1, (1723,386), 3, (0,255,255), -1)
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

    uxt.append(ux)
    uyt.append(uy)
    if i>=4305:
        xxx=int(1955-uy*21.4)
        yyy=int(534-22.04*ux)             
       
    elif i>=4005:
        xxx=int(1955-uy*21.4)
        yyy=int(534-22.04*ux)  
        

    elif i>=2225:
        xxx=int(1955-uy*21.4)
        yyy=int(534-22.04*ux)         
    elif i>1780:
        xxx=int(1955-uy*21.4)
        yyy=int(520-22.04*ux)         
    elif i>980:
        xxx=int(1955-uy*21.4)
        yyy=int(520-22.04*ux)       
    elif i>760:
        xxx=int(1955-uy*21.1)
        yyy=int(520-22.04*ux)       
    elif i>566:
        xxx=int(1955-uy*21.15)
        yyy=int(520-22.04*ux)                    
    else:
        
        xxx=int(1955-uy*21.4)
        yyy=int(515-22.04*ux)    

    cv2.circle(img1,(xxx,yyy),10,(255,0,0),-1)
    cv2.circle(img1,(xxx,yyy),6,(255,255,0),-1) 
    uxl.append(xxx)
    uyl.append(yyy)
       
    for i in range(len(xcl)):
        if i==0:
            continue
        try:
            cv2.line(img1, (xcl[i], ycl[i]), (xcl[i-1], ycl[i-1]), (0, 0, 255), 3)
        except:
            continue
    for i in range(len(uxt)):
        if i==0:
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
            elif i>980:
                cv2.line(img1, (int(1955-uyt[i]*21.4) , int(520-22.04*uxt[i])), (int(1955-uyt[i]*21.4), int(520-22.04*uxt[i])), (255, 0,0), 3)
            elif i>760:
                cv2.line(img1, (int(1955-uyt[i]*21.1) , int(520-22.04*uxt[i])), (int(1955-uyt[i]*21.1), int(520-22.04*uxt[i])), (255, 0,0), 3)
            elif i>566:
                cv2.line(img1, (int(1955-uyt[i]*21.15) , int(520-22.04*uxt[i])), (int(1955-uyt[i]*21.15), int(520-22.04*uxt[i])), (255, 0,0), 3)                        
            else:
                cv2.line(img1, (int(1937-uyt[i]*19.8) , int(555-20.416*uxt[i])), (int(1937-uyt[i]*19.8), int(555-20.416*uxt[i])), (255, 0,0), 3) 
        except:
            continue 
    cv2.imshow('fragme',img1)
    k = cv2.waitKey(30) & 0xFF
    if k == 32:
        break
cap.release()
cv2.destroyAllWindows()