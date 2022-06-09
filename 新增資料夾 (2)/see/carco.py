import time
import serial
import imu
ser=serial.Serial('/dev/ttyUSB_ardco',9600)
class car:
    def __init__(self,move):
        self.move=move
    def forward(race):
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=108
        x[2]=104
        x[3]=race
        x[4]=race
        ser.write(x)
    def left(race):
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=108
        x[2]=108
        x[3]=race
        x[4]=race
        ser.write(x)
    def left2(race):
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=108
        x[2]=108
        x[3]=race
        x[4]=0
        ser.write(x)    
    def right(race):
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=104
        x[2]=104
        x[3]=race
        x[4]=race
        ser.write(x)
    def right2(race):
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=104
        x[2]=104
        x[3]=0
        x[4]=race
        ser.write(x)
    def behind(race):
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=104
        x[2]=108
        x[3]=race
        x[4]=race
        ser.write(x)
    def stop():
        x=bytearray(b'\x66\x68\x68\x00\x45')
        x[1]=104
        x[2]=108
        x[3]=0
        x[4]=0
        ser.write(x)
    def dire(angle,maximu,minimu,oldimu,race1,race2):
        while True:
            
            imur=imu.imu()
            imur=int(imur[0])+360-oldimu
            imuc=angle
            if angle>=maximu:
                imuc=angle-maximu+minimu
            elif angle<= minimu:
                imuc=maximu-(minimu-angle)
            imucbig=imuc+180
            imucsma=imuc-180
            imucmax=imuc+40
            imucmin=imuc-40
            imucmaxx=imuc+10
            imucminn=imuc-10
            imax=0
            imaxx=0
            imbig=0
            
            if imucmaxx>maximu:
                imucmaxx=imucmaxx-maximu+minimu
                imaxx=1
            elif imucminn<minimu:
                imucminn=maximu-(minimu-imucminn)
                imaxx=2
            if imucmax>maximu:
                iimucmax=imucmax-maximu+minimu
                imax=1
            elif imucmin<=minimu:
                imucmin=maximu-(minimu-imucmin)
                imax=2
            if imucbig>maximu:
                imucbig=imucbig-maximu+minimu
                imbig=1
            elif imucsma<minimu:
                imucsma=maximu-(minimu-imucsma)
                imbig=2
            print(imur,imuc,imucmaxx,imucminn)
            if imur<=imucmaxx and imur>=imucminn:
                break
            elif imaxx==1:
                print(1)
                if imur<= imucbig and imuc>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur<=imucmax and imur>imucmaxx:
                    car.right2(race2)
                    status='Rotate right'
                elif imur>imucbig and imur<=imucmin:
                    car.left2(race1)
                elif imur>imucbig and imur<=imucminn:
                    car.left2(race2)
                if imur<= imucmaxx or imur>=imucminn:
                    break
            elif imaxx==2:
                print(2)
                if imur<= imucmin and imur>= imucbig:
                    car.left2(race1)
                    status='Rotate left'
                elif imur< imucminn and imur>=imucmin:
                    car.left2(race2)
                    status='Rotate left'
                elif imur <=imucbig  and imur>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur<=imucmax:
                    car.right2(race2)
                    status='Rotate right'
                if imur>= imucminn or imur<= imucmaxx:
                    break
            elif imax==1:
                print(3)
                if imur<=imucbig and imuc>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur<=imucmax or imur>imucmaxx:
                    car.right2(race2)
                    status='Rotate right'
                elif imur>=imucsma and imur<imucmin:
                    car.left2(race1)
                    status='Rotate left'
                elif imur<imucminn and imur>=imucmin:
                    car.left2(race2)
                    status='Rotate left'
            elif imax==2:
                print(4)
                if imur <=imucbig and imur>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur <=imucmax and imur>imucmaxx:
                    car.right2(race2)
                    status='Rotate right'
                elif imur >=imucsma and imur<=imucmin:
                    car.left2(race1)
                    status='Rotate left'
                elif imur >=imucmin or imur<imucminn:
                    car.left2(race2)
                    status='Rotate left'
            elif imbig==1:
                print(5)
                if imur <=imucbig or imur>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur<= imucmax and imur>imucmaxx:
                    car.right2(race2)
                    status='Rotate right'
                elif imur>=imucsma and imur <=imucmin:
                    car.left2(race1)
                    status='Rotate left'
                elif imur>=imucmin and imur<imucminn:
                    car.left2(race2)
                    status='Rotate left'
            elif imbig==2:
                print(6)
                if imur<=imucbig and imur>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur<= imucmax and imur>imucmaxx:
                    car.right2(race2)
                    status='Rotate right'
                elif imur >=imucsma or imur<imucmin:
                    car.left2(race1)
                    status='Rotate left'
                elif imur>=imucmin and imur<imucminn:
                    car.left2(race2)
                    status='Rotate left'

            else:
                print(7)
                if imur<=imucbig and imur>imucmax:
                    car.right2(race1)
                    status='Rotate right'
                elif imur <=imucmax and imur>imucmaxx:
                    car.right2(race2)
                    status='Rotate right'
                elif imur >= imucsma and imur<imucmin:
                    car.left2(race1)
                    status='Rotate left'
                elif imur>=imucmin and imur<imucminn:
                    car.left2(race2)
                    status='Rotate left'












