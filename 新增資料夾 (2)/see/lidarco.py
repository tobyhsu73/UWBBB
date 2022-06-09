import init
import time
import numpy as np
import math
import numpy as np

port='/dev/ttyUSB_lidar'
Obj=init.YdLidarX4(port)


def getdata():
    
    global gen
    Obj.Connect()
    gen = Obj.StartScanning()
    
         
    data=next(gen)
       
   
def fordata():
    
    ldata={}
    forw=[]
    the=[]
    an=[]
    fl=0
    fr=0
    data=next(gen)
    for i in range(30,-1,-1):
        the.append(i)
    for i in range(30):
        the.append(i)
    for i in range(332,360,1):
        forw.append(data[i])
        if i==359:
            for i in range(30):
              forw.append(data[i])  
                
    
    
    for i in range(0,58):
        an.append(forw[i]*math.cos(math.radians(the[i])))
        
    for i in range(0,58):
        if i<=30:
            if an[i]<=600 and an[i]!=0:
                fl=fl+1
        else:
            if an[i]<=600 and an[i]!=0:
        
                fr=fr+1


    linc=[]
    theli=[]
    an5=[]
    licn=0

    for i in range(30,70):
        linc.append(data[i])

    for i in range(70,30,-1):
        theli.append(i)
    for i in range(40):
        an5.append(linc[i]*math.cos(math.radians(theli[i])))
        if linc[i]*math.cos(math.radians(theli[i]))<=600 and linc[i]*math.cos(math.radians(theli[i]))!=0:
            licn=licn+1

    
    left=[]
    thel=[]
    an2=[]
    leftn=0

    for i in range(70,130,1):
        left.append(data[i])

    for i in range(20,-1,-1):
        thel.append(i)
    for i in range(1,41):
        thel.append(i)
  
    for i in range(60):
        an2.append(left[i]*math.cos(math.radians(thel[i])))
    for i in range(60):
        if an2[i]<=600 and an2[i]!=0:
            leftn=leftn+1
    
    
    
    rinc=[]
    theri=[]
    an4=[]
    rincn=0

    
    for i in range(292,330):
        rinc.append(data[i])
        
    for  i in range(66,28,-1):
        theri.append(i)
        
    for i in range(38):
        an4.append(rinc[i]*math.cos(math.radians(theri[i])))
        if rinc[i]*math.cos(math.radians(theri[i]))<=600 and rinc[i]*math.cos(math.radians(theri[i]))!=0:
            rincn=rincn+1
    
    
    right=[]
    ther=[]
    an3=[]
    rightn=0

    for i in range(252,292):
        right.append(data[i])
        
    
    for i in range(18,-1,-1):
        ther.append(i)
    for i in range(1,22):
        ther.append(i)
    
    for i in range(40):
        an3.append(right[i]*math.cos(math.radians(ther[i])))
    for i in range(40):
        if an3[i]<=650 and an3[i]!=0:
            rightn=rightn+1
    data={'fr':fr,'fl':fl,'leftn':leftn,'rightn':rightn,'rincn':rincn,'licn':licn}
    return data    
if __name__=='__main__':
   
    getdata()
    while True:
        
        data=fordata()
        print(data)