import time
import serial
import carco as co
import imu
import lidarco as lc

ser=serial.Serial('/dev/ttyUSB_OP',19200)
lc.getdata()
ser.flushInput()

def opget():
    c=0
    ser.flushInput()
    while True:
        try:
           
            print('get')
            data1=lc.fordata()
            data=ser.readline()
            print(data)
            data=bytes.decode(data)
            if data[0]=='{':
                data=eval(data)
                c=0
                break
            if  data1['fr']>=2 or data1['fl']>=2:
                data={'angle': 101.751, 'status': 'gg', 'length': 92.8571}
                c=0
                break
            
        except:
            c=c+1
            if c==10:
                cao.car.stop()
            pass
    return data
while True:
    data1=lc.fordata()
    print(data1)
    try:
        
        data=opget()    
        
        
        print(data)
    except:
        co.car.stop()
        continue
    if data['status']=='left' :
        i=0
        while True:
            i=i+1
            data=opget()
            if data['status']=='go':
                break

            else:                
                co.car.right(40)
            
    elif data['status']=='right':
        i=0
        while True:
            i=i+1
            data=opget()
            if data['status']=='go':
                break

            else:                
                co.car.left(30)
        
    elif  data['status']=='forward':
        break
    if data1['fr']>=3 or data1['fl']>=3:
        print('ulllll')
        if data1['fr']>data1['fl']:
            i=0
            while True:
                print('ulllll')
                
                data1=lc.fordata()
                print(data1)
                if data1['fr']>=2 or data1['fl']>=2:
                    i=i+1

                    co.car.right(30)
                elif data1['rightn']>3 or data1['rincn']>3:
                    co.car.forward(40)
                else:
                    break
        else:
            i=0
            while True:
                print('ulllll')
                data1=lc.fordata()
                print(data1)
                if data1['fr']>=2 or data1['fl']>=2:

                    co.car.left(30)
                    
                    
                elif data1['leftn']>3 or data1['licn']>3:
                    co.car.forward(40)
                else:
                    break

    if data['status']=='go' and data['angle']>104:
        co.car.left2(70)
        
    elif data['status']=='go' and data['angle']<96:
        
        co.car.right2(60)
        print(1)
    elif data['status']=='go':
        co.car.forward(70)

    elif data['status']=='none':
        co.car.stop()
        print(3)

    #break
co.car.stop()
    
    
                 
    


      
        
    
    
