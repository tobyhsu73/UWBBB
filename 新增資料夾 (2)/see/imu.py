import struct
import serial
oldimu=1
def imu():
    ser = serial.Serial('/dev/ttyUSB_gyro',115200)
    ser.flushInput()
    count=0
    
    while True:
        data=ser.read(1)
        count+=1
        if data[0]==0x5A:
            data=ser.read(1)
            if data[0]==0xA5:
                data=ser.read(1)
                if data[0]==76:
                    data=ser.read(1)
                    if data[0]==0:
                        break
            else:
                pass
        else:
            pass
        
    data=ser.read(2)
    data=ser.read(1)
    data=ser.read(1)
    data=ser.read(6)
    data=ser.read(4)
    time_stamp=struct.unpack('I',data)
    data=ser.read(4)
    x_acc=struct.unpack('<f',data)
    data=ser.read(4)
    y_acc=struct.unpack('<f',data)
    data=ser.read(4)
    z_acc=struct.unpack('<f',data)
    data=ser.read(4)
    x_gyr=struct.unpack('<f',data)
    data=ser.read(4)
    y_gyr=struct.unpack('<f',data)
    data=ser.read(4)
    z_gyr=struct.unpack('<f',data)
    data=ser.read(4)
    x_mag=struct.unpack('<f',data)
    data=ser.read(4)
    y_mag=struct.unpack('<f',data)
    data=ser.read(4)
    z_mag=struct.unpack('<f',data)
    data=ser.read(4)
    roll_eul=struct.unpack('<f',data)
    data=ser.read(4)
    pitch_eul=struct.unpack('<f',data)
    data=ser.read(4)
    yaw_eul=struct.unpack('<f',data)
    ser.close()
    return yaw_eul

def zero():
    oldimu=0
    imunum=0
    while True:
        imur=imu()
        imur=int(imur[0])
        if imur-oldimu<=3:
            imunum=imunum+1
        else:
            imunum=0
        oldimu=imur
        if imunum>=10:
            if oldimu>0:
                maximu=180-oldimu+360
                minimu=maximu-360
            elif oldimu<0:
                minimu=180-oldimu
                maximu=minimu+360
            break
    print(oldimu,maximu,minimu)
    return oldimu,maximu,minimu
    
    
while __name__=='__main__':
    print(imu())
    
    