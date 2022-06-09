import time
import serial
import numpy as np
import struct
    
ser=serial.Serial('/dev/ttyUSB_uwb',115200)

ser.bytesize = serial.EIGHTBITS 
ser.parity =serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE 
ser.timeout = 0.3
ser.flushInput()
i=0
ser.write(b'\r\r')   # enter shell mode from generic mode
time.sleep(1)
ser.write(b'lec\r')
print('begin')

def firstread():
    while True:
        try:
    
            ser.flushInput()
            data=ser.readline()
            print(data)
            #print('this is 1')

            ct=0

               #print('this is ct',ct)
            if len(data)==0:

                ser.write(b'\r\r')   # enter shell mode from generic mode
                ser.write(b'lec\r')
                print('begin')# return to shell mode
                time.sleep(0.1)
                
                pass

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
            data=str(data)       # convert bytes to string
            data = data.replace("\r\n", "")  # to remove \r\n in string
                    #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
            print(data)
            
                    
            ###time.sleep(0.01)
                                                  
            if (("DIST" in data) and ("AN0" in data) and ("AN1" in data) and ("AN2" in data) and ("AN3" in data)):
                                            
               data = data.split(",")   # splitting string 
               anchor_info={'Anchor No':[],'AID':[],'Ax':[],'Ay':[],'Az':[],'ADist':[]}
            else:
                pass
                    
               
               #print(data_dict)
                            #print('data after splitting')
                            #print(data)
                            # the class of data is 'list' with [ ]
                            #print(type(data))
            if("DIST" in data):
                anchor_Nummber = int(data[data.index("DIST")+1])  #最大是4
                
                #anchor_Nummber = int(4)
                for i in range(anchor_Nummber):
                    anchor_data = {"id": data[data.index("AN"+str(i))+1], "x": data[data.index("AN"+str(i))+2],
                                 "y": data[data.index("AN"+str(i))+3],"z": data[data.index("AN"+str(i))+4],
                                 "dist": data[data.index("AN"+str(i))+5]}
                                    # the class of pos_AN is 'dict'
                   # print(anchor_info)
                    anchor_info['Anchor No'].append(data[data.index("AN"+str(i))])
                    anchor_info['AID'].append(data[data.index("AN"+str(i))+1])
                    anchor_info['Ax'].append(data[data.index("AN"+str(i))+2])
                    anchor_info['Ay'].append(data[data.index("AN"+str(i))+3])
                    anchor_info['Az'].append(data[data.index("AN"+str(i))+4])
                    anchor_info['ADist'].append(data[data.index("AN"+str(i))+5])
                                 
                if("POS" in data):
                    
                                        
                    pos = {'x': data[data.index('POS')+1],
                            'y': data[data.index('POS')+2],
                            'z': data[data.index('POS')+3]}
                    i=1
                    
                    pos['x']=float(pos['x'])
                    pos['y']=float(pos['y'])
                    pos['z']=float(pos['z'])
                    break

                                                 
                    

       
        except:
            pass

    return pos, anchor_info
        
    
def uwbread():
    s=0
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
            data=str(data)       # convert bytes to string
            data = data.replace("\r\n", "")  # to remove \r\n in string
                    #data=data.rstrip("\r\n")         # or using rstrip to remove \r\n
            print(data)
            
                    
            ###time.sleep(0.01)
                                                  
            if (("DIST" in data) and ("AN0" in data) and ("AN1" in data) and ("AN2" in data) and ("AN3" in data)):
                                            
               data = data.split(",")   # splitting string 
               anchor_info={'Anchor No':[],'AID':[],'Ax':[],'Ay':[],'Az':[],'ADist':[]}
            else:
                pass
                    
               
               #print(data_dict)
                            #print('data after splitting')
                            #print(data)
                            # the class of data is 'list' with [ ]
                            #print(type(data))
            if("DIST" in data):
                anchor_Nummber = int(data[data.index("DIST")+1])  #最大是4
                
                #anchor_Nummber = int(4)
                for i in range(anchor_Nummber):
                    anchor_data = {"id": data[data.index("AN"+str(i))+1], "x": data[data.index("AN"+str(i))+2],
                                 "y": data[data.index("AN"+str(i))+3],"z": data[data.index("AN"+str(i))+4],
                                 "dist": data[data.index("AN"+str(i))+5]}
                                    # the class of pos_AN is 'dict'
                   # print(anchor_info)
                    anchor_info['Anchor No'].append(data[data.index("AN"+str(i))])
                    anchor_info['AID'].append(data[data.index("AN"+str(i))+1])
                    anchor_info['Ax'].append(data[data.index("AN"+str(i))+2])
                    anchor_info['Ay'].append(data[data.index("AN"+str(i))+3])
                    anchor_info['Az'].append(data[data.index("AN"+str(i))+4])
                    anchor_info['ADist'].append(data[data.index("AN"+str(i))+5])
                                 
                if("POS" in data):
                    
                                        
                    pos = {'x': data[data.index('POS')+1],
                            'y': data[data.index('POS')+2],
                            'z': data[data.index('POS')+3]}
                    i=1
                    
                    pos['x']=float(pos['x'])
                    pos['y']=float(pos['y'])
                    pos['z']=float(pos['z'])

                                                 
                    


        except:
            pass
                
    return pos, anchor_info

    #return tag_pos

if __name__=='__main__':
    while True:
        
        a,b=uwbread()
        print(a,b)