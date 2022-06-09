# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:04:14 2022

@author: Young_BoyFriend
"""
dataname='k1.txt'
x1=[]
y1=[]

x2=[]
y2=[]

data1={}
data2={}
with open(dataname,'r') as f:
    for d in f.readlines():
        d2=d.replace(" ","").split("]")[0].split("[")[1].replace(","," ").replace("'","").split(" ")
        if d2[1]=='0':
            x1.append(float(d2[3]))
            y1.append(float(d2[4]))
        elif d2[1]=='1':
            x2.append(float(d2[3]))
            y2.append(float(d2[4]))

data1['x']=x1
data1['y']=y1
data2['x']=x2
data2['y']=y2

r1 = open('k1_1.txt', 'w')
r1.write(str(data1))
r1.close()

r2 = open('k1_2.txt', 'w')
r2.write(str(data2))
r2.close()
