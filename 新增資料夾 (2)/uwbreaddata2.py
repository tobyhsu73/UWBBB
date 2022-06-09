import time
import serial
import numpy as np
import struct
import givedataul

def uwbread():
    while True:
        
    
        
        data=givedataul.getdata()
        #ser.flushInput()
        #data=ser.readline()
        
        #print('this is 1')

        ct=0

           #print('this is ct',ct)


           #print(ct,'\r',data)
           
    #     print(data)
    #     print('this is 2')
    #     data=ser.readline()
    #     print(data)
    #     print('this is 3')
        #print('data transfer as follows')
       
                    
            # class 'bytes'
        
            # decoding to UTF-8 format
               # convert bytes to string
        
                #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
        data=data.split(',')
        x=float(data[3])
        y=float(data[4])
        print(1)
        int(x)
        
        s=1
        
        break

    return x,y,s
if __name__=='__main__':
    while True:
        
        uwbread()
