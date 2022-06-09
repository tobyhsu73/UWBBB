import time
import serial
import numpy as np
import struct
    
ser=serial.Serial('com31',115200)

ser.bytesize = serial.EIGHTBITS 
ser.parity =serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE 
ser.timeout = 0.5
ser.flushInput()
i=0
ser.write(b'\r\r')   # enter shell mode from generic mode
time.sleep(1)
ser.write(b'lec\r')
print('begin')

def uwbread():
    while True:
        
        try:
            
        
            ser.flushInput()
            data=ser.readline()
            
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
            data=ser.readline()
            data=data.decode()     # decoding to UTF-8 format
                   # convert bytes to string
            data = data.replace("\r\n", "")  # to remove \r\n in string
                    #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
            data=data.split(',')
            x=float(data[3])
            y=float(data[4])
            z=float(data[5])
            s=1
            break
        except:
                pass
    return x,y,z,s
if __name__=='__main__':
    while True:
        
        x,y,z,s=uwbread()
        dic={'x':x,'y':y,'z':z}
        dic=str(dic)
        f=open('w2.txt','a')
        f.write(dic+'\n')
        f.close()
        print(x,y,z,s)
        