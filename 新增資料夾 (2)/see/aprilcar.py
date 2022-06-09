import time
import serial
import carco as co
ser=serial.Serial('/dev/ttyUSB_OP',19200)
z=0
oldangle=90
def opget():
    c=0
    ser.flushInput()
    while True:
        try:
            data=ser.readline()
            data=bytes.decode(data)
            if data[0]=='{':
                data=eval(data)
                c=0
                break
            
        except:
            c=c+1
            if c==10:
                co.car.stop()
            pass
    return data
while True:
    try:
        
        data=opget()
        print(data)
        length=abs(data['length'])
        if length<=10:
            co.car.stop()
        elif data['angle']==oldangle:
            z=z+1
            if z==2:
                z=0
                co.car.stop()
        
        elif data['status']=='go' and data['angle']>106:
            co.car.left2(70)
            
        elif data['status']=='go' and data['angle']<94:
            
            co.car.right2(60)
            print(1)
        elif data['status']=='go':
            co.car.forward(80)
        oldangle=data['angle']
    except:
        pass

