import time
import lidarco as lc
import carco as co
lc.getdata()
while True:
    

    data1=lc.fordata()
    print(data1)
    if data1['fr']>=3 or data1['fl']>=3:
        if data1['fr']>data1['fl']:
            i=0
            while True:
                print(data1)
                data1=lc.fordata()
                if data1['fr']>=3 or data1['fl']>=3:
                    i=i+1
                    if i>3:
                        co.car.stop()
                        i=0
                        continue
                    co.car.right(70)
                elif data1['rightn']>3 or data1['rincn']>3:
                    co.car.forward(70)
                else:
                    break
        else:
            i=0
            while True:
                data1=lc.fordata()
                print(data1)
                if data1['fr']>=3 or data1['fl']>=3:
                    i=i+1
                    if i>3:
                        co.car.stop()
                        i=0
                        continue
                    co.car.left(70)
                    
                    
                elif data1['leftn']>3 or data1['licn']>3:
                    co.car.forward(70)
                else:
                    break
    else:
        co.car.forward(70)
                