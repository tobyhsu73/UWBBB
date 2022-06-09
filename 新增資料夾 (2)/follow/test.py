import serial
import time
import imu
import paho.mqtt.client as mqtt
#broker_address='broker.emqx.io'
#client=mqtt.Client('g2')
#client.connect(broker_address)
second=str(int(time.time()))
print(time.time())
x=0x3A,0x30,0x31,0x30,0x33,0x31,0x34,0x35,0x36,0x30,0x30,0x30,0x34,0x38,0x45,0x0D,0x0A
ser=serial.Serial('/dev/ttyUSB1',9600,bytesize=7,parity='E',stopbits=1)

    
while True:
    ser.write(x)
    r=ser.readline()
    r=r.decode()
    i=imu.imu()
    i=i[0]
    lsd1=r[7]+r[8]+r[9]+r[10]
    lsd2=r[11]+r[12]+r[13]+r[14]
    lsd3=r[15]+r[16]+r[17]+r[18]
    lsd4=r[19]+r[20]+r[21]+r[22]
    rf=(int(lsd1,16)-27)*(950/1623)+50
    rb=(int(lsd2,16)-23)*(950/1615)+50#rb
    lf=(int(lsd3,16)-21)*(950/2012)+50#lf
    lb=(int(lsd4,16)-11)*(950/2001)+50#lb
    
    dic={'lf':lf,'rf':rf,'rb':rb,'lb':lb,'time':time.time(),'imu':i}
    dic=str(dic)
    #client.publish('laser',dic)
    f=open(second+'.txt','a')
    f.write(dic+'\n')
    f.close()
    

    #print(lf,rf,lb,rb)
    print(lf)
    #print(f,b,f-b)
    
    #print('PLC讀取值',lsd,' 轉換後雷射距離',lsdr,'mm')

