import time
import serial
ser=serial.Serial('/dev/ttyUSB_OP',19200)
ser.flushInput()
while True:
    print(123)
    data=ser.readline()
    print(data)
    time.sleep(0.001)