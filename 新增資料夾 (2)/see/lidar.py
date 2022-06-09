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
    if(Obj.Connect()):
        gen = Obj.StartScanning()
    
         
        data=next(gen)
       
    return data

def fordata():
    ldata={}
    forw=[]
    the=[]
    an=[]
    fl=0
    fr=0
    data=next(gen)
    for i in range(32,-1,-1):
        the.append(i)
    for i in range(1,23):
        the.append(i)
    for i in range(58,109):
        forw.append(data[i])
    
    
    for i in range(0,50):
        an.append(forw[i]*math.cos(math.radians(the[i])))
        
    for i in range(0,50):
        if i<=25:
            if an[i]<=1000 and an[i]!=0:
                fl=fl+1
        else:
            if an[i]<=1000 and an[i]!=0:
        
                fr=fr+1                

    left=[]
    thel=[]
    an2=[]
    leftn=0

    for i in range(28,-1,-1):
        left.append(data[i])
        
        if i==0:
            for i in range(359,336,-1):
                left.append(data[i])
    for i in range(30,-1,-1):
        thel.append(i)
    for i in range(1,22):
        thel.append(i)
  
    for i in range(52):
        an2.append(left[i]*math.cos(math.radians(thel[i])))
    for i in range(52):
        if an2[i]<=650 and an2[i]!=0:
            leftn=leftn+1
            


    right=[]
    ther=[]
    an3=[]
    rightn=0

    for i in range(151,207):
        right.append(data[i])
        
    
    for i in range(26,-1,-1):
        ther.append(i)
    for i in range(1,30):
        ther.append(i)
    
    for i in range(56):
        an3.append(right[i]*math.cos(math.radians(ther[i])))
    for i in range(56):
        if an3[i]<=650 and an3[i]!=0:
            rightn=rightn+1    
 

    rinc=[]
    theri=[]
    an4=[]
    rincn=0

    
    for i in range(110,150):
        rinc.append(data[i])
        
    for  i in range(20,60):
        theri.append(i)
        
    for i in range(40):
        an4.append(rinc[i]*math.cos(math.radians(theri[i])))
        if rinc[i]*math.cos(math.radians(theri[i]))<=1000 and rinc[i]*math.cos(math.radians(theri[i]))!=0:
            rincn=rincn+1
  
    

    linc=[]
    theli=[]
    an5=[]
    licn=0

    for i in range(30,67):
        linc.append(data[i])

    for i in range(60,23,-1):
        theli.append(i)
    for i in range(37):
        an5.append(linc[i]*math.cos(math.radians(theli[i])))
        if linc[i]*math.cos(math.radians(theli[i]))<=1000 and linc[i]*math.cos(math.radians(theli[i]))!=0:
            licn=licn+1
   
    beh=[]
    theb=[]
    an6=[]
    behn=0

    for i in range(250,286):
        beh.append(data[i])
    for i in range(20,-1,-1):
        theb.append(i)
        if i==0:
            for i in range(1,16):
                theb.append(i)
 
    for i in range(36):
        an6.append(beh[i]*math.cos(math.radians(theb[i])))
        if beh[i]*math.cos(math.radians(theb[i]))<=1000 and beh[i]*math.cos(math.radians(theb[i]))!=0:
            behn=behn+1

    rbinc=[]
    therbi=[]
    an7=[]
    rbincn=0

    
    for i in range(221,252):
        rbinc.append(data[i])
        
    for  i in range(41,72):
        therbi.append(i)
 
        
    for i in range(31):
        an7.append(rbinc[i]*math.cos(math.radians(therbi[i])))
        if rbinc[i]*math.cos(math.radians(therbi[i]))<=1000 and rbinc[i]*math.cos(math.radians(therbi[i]))!=0:
            rbincn=rbincn+1
    
    

      

    lbinc=[]
    thelbi=[]
    an8=[]
    lbinc=[]
    lbincn=0

    for i in range(293,333):
        lbinc.append(data[i])
   
    for i in range(23,63):
        thelbi.append(i)
    for i in range(40):
        an8.append(lbinc[i]*math.cos(math.radians(thelbi[i])))
        if lbinc[i]*math.cos(math.radians(thelbi[i]))<=1000 and lbinc[i]*math.cos(math.radians(thelbi[i]))!=0:
            lbincn=lbincn+1
    
    lidard={'fl':fl,'fr':fr,'leftn':leftn,'rightn':rightn,'rincn':rincn,'licn':licn,'rbincn':rbincn,'lbincn':lbincn}
    print(lidard)



if __name__=='__main__':
   
    getdata()
    while True:
        
        fordata()