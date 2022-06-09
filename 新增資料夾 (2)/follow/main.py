import time
import uwbread as uwb
import motor
from PID import PID
import math
import serial
import test
pid=PID(p=2,i=0.5,d=0.01,imax=10)
motor.begin('/dev/ttyUSB_ardco')
#centor 0.3,0.23
def caruwb():
    while True:
        print(123)
        x,y,s=uwb.uwbread()
        try:
            int(x)
        except:
            continue
      
        dis=((abs(x-0.3))**2+(abs(y-0.23))**2)**0.5
        print(dis)
        m1=0
        if y-0.23==0:
            print('pass')
            continue
        m2=(x-0.3)/(y-0.23)
        angle=m1-m2
        angle=math.degrees(math.atan(angle))
        if y<=0.23 and x>=0.3:
            angle=-90-angle
        elif y<=0.23 and x<0.3:
            angle=90-angle
        print(angle)
        break
    return dis,angle,s
    #return dis
while True:
    dis,angle,s=caruwb()
    output=pid.get_pid(angle,1)
    test.readdata()
    if s==0:

        continue
    elif dis<=0.7:
    
        motor.go(0,0)
    elif s==1:
        
            
                
        a=int(100-output)
        b=int(100+output)
        if a>250:
            a=250
        if b>250:
            b=250
        print(a,b,output)
        motor.go(a,b)
        print(55555555555)


    
    
        
    
        
    
 

        
        
