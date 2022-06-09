import init
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import numpy as np

port='COM19'
Obj=init.YdLidarX4(port)


def getdata():
    
    global gen
    Obj.Connect()
    gen = Obj.StartScanning()
    
         
    data=next(gen)
       
    return data

def fordata():
    data=next(gen)
    forw=[]
    forl=[]
    an=[]
    forrn=0
    forln=0
    for i in range(11,-1,-1):
        forw.append(data[i])
        
        if i==0:
            for i in range(359,339,-1):
                forw.append(data[i])
    for i in range(11,-1,-1):
        forl.append(i)
    for i in range(1,20):
        forl.append(i)
  
    for i in range(31):
        an.append(int(forw[i]*math.cos(math.radians(forl[i]))))
        if an[i]<750 and an[i]!=0 and i<11:
            forln=forln+1
        elif an[i]<750 and an[i] !=0:
            forrn=forrn+1
    '''
    lef
    '''
    linc=[]
    left=[]
    lefti=[]
    an2=[]
    leftn=0

    
    for i in range(310,339):
        linc.append(data[i])
        
    for  i in range(40,69):
        lefti.append(i)
        
    for i in range(29):
        an2.append(int(linc[i]*math.cos(math.radians(lefti[i]))))
        if linc[i]*math.cos(math.radians(lefti[i]))<=700 and linc[i]*math.cos(math.radians(lefti[i]))!=0:
            leftn=leftn+1

    
    lf=[]
    lfn=0
    lfi=[]
    an3=[]
    '''
    left
    '''
    for i in range(271,310):
        lf.append(data[i])
    for i in range(1,40):
        lfi.append(i)
    for i in range(39):
        an3.append(int(lf[i]*math.cos(math.radians(lfi[i]))))
        if an3[i]<=700 and an3[i] !=0:
            lfn=lfn+1

    '''
    rf
    '''
    rinc=[]
    theli=[]
    an5=[]
    ricn=0

    for i in range(12,45):
        rinc.append(data[i])

    for i in range(78,45,-1):
        theli.append(i)
    for i in range(33):
        an5.append(int(rinc[i]*math.cos(math.radians(theli[i]))))
        if rinc[i]*math.cos(math.radians(theli[i]))<=700 and rinc[i]*math.cos(math.radians(theli[i]))!=0:
            ricn=ricn+1
    print(ricn)
    '''
    rigght
    '''
    rf=[]
    rfn=0
    rfi=[]
    an4=[]
    for i in range(45,80):
        rf.append(data[i])
    for i in range(45,10,-1):
        rfi.append(i)
    for i in range(35):
        an4.append(int(rf[i]*math.cos(math.radians(rfi[i]))))
        if an4[i]<=700 and an4[i]!=0:
            rfn=rfn+1
    
   
    
    
if __name__=='__main__':
   
    getdata()
    while True:
        
        fordata()