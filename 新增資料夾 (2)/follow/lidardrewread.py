
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
f=open('lidardata2.txt','r')

def getdata():
    
    z=f.readline()
    z=eval(z)
    return z
x=[]
y=[]

data=getdata()
for i in range(360):
    x.append(math.radians(i))
for i in range(360):
    y.append(data[i])
figure = plt.figure(figsize=(6,6))

ax=plt.subplot(polar=True)
ax.scatter(x,y,s=10)

def update(frame_number):
    ax.clear()
    a=[]
    b=[]
    c=[]
    
    for i in range(360):
        if i%2==0:
            continue
        c.append(i)
    data=getdata()
    for i in range(360):
        if data[i]>=4000:
            data[i]=0
    

    for i in range(360):
        a.append(math.radians(i))
    for i in range(360):
        b.append(data[i])
    
    ax.scatter(a,b,s=10)
    #plt.thetagrids(c)

ani = FuncAnimation(figure,
                    
                    update,
                    
                    interval=200)
plt.show()