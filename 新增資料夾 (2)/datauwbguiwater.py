import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import time
import numpy as np
import math
import givedataul


S_cale =8
Title_1 = "UlcarGui"  #視窗標題
Title_2 = "介面"
second=str(int(time.time()))


   
#def deg_(xy):    #繪布座標轉換
    #x0~500  y0~1900
    #比例 1:100  (公尺)
   # y=1150-xy*S_cale
   # x=400+xy*S_cale
   # return [x,y]

def motion(win):
    def chan(a,b,c,d):
        global angle
        pointxc=220
        pointyc=300
        ax=(a-pointxc)*math.cos(angle)-(b-pointyc)*math.sin(angle)+pointxc
        ay=(a-pointxc)*math.sin(angle)+(b-pointyc)*math.cos(angle)+pointyc
        bx=(c-pointxc)*math.cos(angle)-(d-pointyc)*math.sin(angle)+pointxc
        by=(c-pointxc)*math.sin(angle)+(d-pointyc)*math.cos(angle)+pointyc
        return ax,ay,bx,by
    

    num=0
    
    
    
    win.title(Title_2)
    win.geometry('1920x1080')

    x=tk.DoubleVar()
    y=tk.DoubleVar()
    olddx=x
    olddy=x
    x.set(x)
    y.set(y)
   
    
    cvs = tk.Canvas(win, width=1200, height=520, bg='white')  #建立畫布(在1080P螢幕上測量)
    cvs.pack(side='left',fill="both",expand="yes")
  
    dx=10
    dy=10
    scale=S_cale # 比例尺，or 450/9, scale from physical space to canvas pixel
    
    # coordinate transformation between Map and Canvas
    
    X0=450   # 笛卡爾座標原點x相對於畫布的原點
    Y0=800
    

    i=0
    allpath=0
    #anchor
    r=5
    Imacar = Image.open("water.png")
    photo2=ImageTk.PhotoImage(Imacar.rotate(0))
        #photo2=ImageTk.PhotoImage(Imacar.rotate(260))
    imag2=cvs.create_image(-8.2*scale+X0,-102*scale+Y0,anchor=tk.NW,image=photo2)
    cvs.create_line(0*scale+X0,0*scale+Y0,0*scale+X0,-50*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(10*scale+X0,0*scale+Y0,10*scale+X0,-50*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(20*scale+X0,0*scale+Y0,20*scale+X0,-50*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(30*scale+X0,0*scale+Y0,30*scale+X0,-50*scale+Y0, fill='white', width=1,dash=(4,4))
 
    cvs.create_line(0*scale+X0,0*scale+Y0,30*scale+X0,0*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(0*scale+X0,-40*scale+Y0,30*scale+X0,-40*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(0*scale+X0,-10*scale+Y0,30*scale+X0,-10*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(0*scale+X0,-30*scale+Y0,30*scale+X0,-30*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(0*scale+X0,-20*scale+Y0,30*scale+X0,-20*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_line(0*scale+X0,-50*scale+Y0,30*scale+X0,-50*scale+Y0, fill='white', width=1,dash=(4,4))
    cvs.create_text(0*scale+X0,2*scale+Y0, text='0m',fill='white',font=('Arial', 12))
    cvs.create_text(10*scale+X0,2*scale+Y0, text='10m',fill='white',font=('Arial', 12))
    cvs.create_text(20*scale+X0,2*scale+Y0, text='20m',fill='white',font=('Arial', 12))
    cvs.create_text(29*scale+X0,2*scale+Y0, text='30m',fill='white',font=('Arial', 12))
    cvs.create_text(-3*scale+X0,-10*scale+Y0, text='10m',fill='white',font=('Arial', 12))
    cvs.create_text(-3*scale+X0,-20*scale+Y0, text='20m',fill='white',font=('Arial', 12))
    cvs.create_text(-3*scale+X0,-30*scale+Y0, text='30m',fill='white',font=('Arial', 12))
    cvs.create_text(-3*scale+X0,-40*scale+Y0, text='40m',fill='white',font=('Arial', 12))
    cvs.create_text(-3*scale+X0,-50*scale+Y0, text='50m',fill='white',font=('Arial', 12))

    
    
    
    
    cvs.create_oval(0*scale+X0-r,-10*scale-r+Y0,0*scale+X0+r,-10*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(0*scale+X0-r,0*scale-r+Y0,0*scale+X0+r,0*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(0*scale+X0-r,-20*scale-r+Y0,0*scale+X0+r,-20*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(0*scale+X0-r,-30*scale-r+Y0,0*scale+X0+r,-30*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(0*scale+X0-r,-40*scale-r+Y0,0*scale+X0+r,-40*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(0*scale+X0-r,-50*scale-r+Y0,0*scale+X0+r,-50*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(12.2*scale+X0-r,0*scale-r+Y0,12.2*scale+X0+r,0*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(24.4*scale+X0-r,0*scale-r+Y0,24.4*scale+X0+r,0*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(24.4*scale+X0-r,-10*scale-r+Y0,24.4*scale+X0+r,-10*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(24.4*scale+X0-r,-20*scale-r+Y0,24.4*scale+X0+r,-20*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(24.4*scale+X0-r,-30*scale-r+Y0,24.4*scale+X0+r,-30*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(24.4*scale+X0-r,-40*scale-r+Y0,24.4*scale+X0+r,-40*scale+r+Y0, fill='blue', width=2)
    cvs.create_oval(24.4*scale+X0-r,-50*scale-r+Y0,24.4*scale+X0+r,-50*scale+r+Y0, fill='blue', width=2)
    

    while True:
        start=time.time()
        #time.sleep(0.04)
        data=givedataul.getdata()
        x=data['x']
        y=data['y']

        i=i+1
        num=num+1
        dxx=x
        dyy=y
        if num%2==0:
            
            path=((dxx-olddx)**2+(dyy-olddy)**2)**0.5
            allpath=allpath+path
        
            print(allpath)
        olddx=dxx
        olddy=dyy

        mat_1=np.array([[1,0],[0,-1]])    #座標轉換矩陣
        trans=np.array([[X0,Y0]])     # 1-by-u2 translation array
        
        
        kpt=np.array([[1,6],[4,1]])
        kp=np.ones((2,1))*trans + scale*kpt.dot(mat_1)
            #畫當前路徑
 
        r=10  # radius
        spoint=[]
        
        #==============================
        #===============畫車子===============        
   # rotate image by 30 degrees
   
        car_x2=(float(x))  #車子座標        
        car_y2=(float(y))
        
        
        try:
            
            car_x1+1  #此句用於測試car_x1是否存在，不存在即是第一次運行，則例外處理car1先設為car2
            
        except:
            car_x1 = car_x2
            car_y1 = car_y2
        if i==423 or i==862 or i==1267 or i==1650:
            car_x1 = car_x2
            car_y1 = car_y2            
       
        car=np.array([[car_x1,car_y1],[car_x2,car_y2]])
        car2=np.ones((2,1))*trans + scale*car.dot(mat_1)
        r=5
        

                  
        #cvs.create_line(car2[0][0], car2[0][1], car2[1][0], car2[1][1], fill='darkblue', width=0.5)
        cvs.create_oval(car2[0][0]-2,car2[0][1]-2,car2[0][0]+2,car2[0][1]+2, fill="yellow", outline='yellow') 
        cardot=cvs.create_oval(car2[0][0]-10,car2[0][1]-10,car2[0][0]+10,car2[0][1]+10, fill="red")
                
        #==============================
        '''
        cvs.create_polygon (2.3*scale+X0, -3.9*scale+Y0, 1.45*scale+X0,  -4.65*scale+Y0, 2.15*scale+X0, -6*scale+Y0, 2.9*scale+X0, -5.6*scale+Y0,  fill='yellow')
        cvs.create_polygon (1.25*scale+X0, -6.9*scale+Y0, 0.8*scale+X0,  -6.85*scale+Y0, 0.7*scale+X0, -7.2*scale+Y0, 0.55*scale+X0, -7.4*scale+Y0,1.2*scale+X0, -8.5*scale+Y0,1.6*scale+X0, -7.65*scale+Y0,1.75*scale+X0, -7.65*scale+Y0,1.75*scale+X0, -7.25*scale+Y0,1.25*scale+X0, -7.25*scale+Y0,  fill='yellow')
        cvs.create_polygon (1.8*scale+X0, -9.1*scale+Y0, 1.2*scale+X0,  -9.65*scale+Y0, 1.95*scale+X0, -10*scale+Y0, 2.4*scale+X0, -9.65*scale+Y0,  fill='yellow')
        cvs.create_polygon (4.25*scale+X0, -7.6*scale+Y0, 3.8*scale+X0,  -7.6*scale+Y0, 4.5*scale+X0, -7.75*scale+Y0, 4.7*scale+X0, -7.6*scale+Y0,  fill='yellow')
        cvs.create_polygon (3.6*scale+X0, -1.8*scale+Y0, 3.6*scale+X0,  -2.6*scale+Y0, 4.4*scale+X0, -2.6*scale+Y0, 4.4*scale+X0, -1.8*scale+Y0,  fill='yellow')
        cvs.create_polygon (7.8*scale+X0, -2.6*scale+Y0, 7.9*scale+X0,  -2.5*scale+Y0, 8.3*scale+X0, -2.5*scale+Y0, 8.25*scale+X0, -2.45*scale+Y0,  fill='yellow')
        cvs.create_polygon (3.6*scale+X0, -9.85*scale+Y0, 3.6*scale+X0,  -10.65*scale+Y0, 4.4*scale+X0, -10.65*scale+Y0, 4.4*scale+X0, -9.85*scale+Y0,  fill='yellow')
        cvs.create_polygon (7.1*scale+X0, -9.35*scale+Y0, 7.3*scale+X0,  -9.6*scale+Y0, 7.85*scale+X0, -9.35*scale+Y0, 7.7*scale+X0, -9.15*scale+Y0,  fill='yellow')
        cvs.create_line(10.2*scale+X0,-5.5*scale+Y0,9.9*scale+X0,-5.9*scale+Y0, fill="yellow",width=10)
        cvs.create_polygon (10.4*scale+X0, -4.5*scale+Y0, 10.25*scale+X0,  -4.65*scale+Y0, 10.6*scale+X0, -4.95*scale+Y0, 10.75*scale+X0, -4.95*scale+Y0,  fill='yellow')
        cvs.create_polygon (11.8*scale+X0, -5.9*scale+Y0, 11.4*scale+X0,  -5.9*scale+Y0, 12.1*scale+X0, -6.05*scale+Y0, 12.15*scale+X0, -5.65*scale+Y0,  fill='yellow')
        cvs.create_line(11.7*scale+X0,-3.85*scale+Y0,13.0*scale+X0,-3.85*scale+Y0, fill="yellow",width=10)
        cvs.create_line(13.0*scale+X0,-5.4*scale+Y0,13.0*scale+X0,-3.85*scale+Y0, fill="yellow",width=10)
        cvs.create_polygon(5.25*scale+X0, -4.5*scale+Y0, 5.25*scale+X0,  -7*scale+Y0, 8.6*scale+X0, -7.3*scale+Y0, 8.6*scale+X0, -5.3*scale+Y0,8.4*scale+X0, -5.3*scale+Y0,8.4*scale+X0, -6.8*scale+Y0,5.5*scale+X0, -6.85*scale+Y0,5.5*scale+X0, -5.5*scale+Y0,6.1*scale+X0, -5*scale+Y0,6.1*scale+X0, -4.5*scale+Y0,  fill='yellow')
        cvs.create_line(10.55*scale+X0,-9.3*scale+Y0,10.55*scale+X0,-7.7*scale+Y0, fill="yellow",width=5)
        cvs.create_line(10.55*scale+X0,-7.7*scale+Y0,12.5*scale+X0,-7.7*scale+Y0, fill="yellow",width=5)
        cvs.create_line(12.5*scale+X0,-7.7*scale+Y0,12.5*scale+X0,-9.3*scale+Y0, fill="yellow",width=5)
        cvs.create_polygon (8.6*scale+X0, -1.8*scale+Y0, 8.6*scale+X0,  -2.6*scale+Y0, 9.4*scale+X0, -2.6*scale+Y0, 9.4*scale+X0, -1.8*scale+Y0,  fill='yellow')
        cvs.create_polygon (8.6*scale+X0, -9.85*scale+Y0, 8.6*scale+X0,  -10.65*scale+Y0, 9.4*scale+X0, -10.65*scale+Y0, 9.4*scale+X0, -9.85*scale+Y0,  fill='yellow')
        cvs.create_polygon (3.6*scale+X0, -1.8*scale+Y0, 3.6*scale+X0,  -2.6*scale+Y0, 4.6*scale+X0, -2.6*scale+Y0, 4.6*scale+X0, -1.8*scale+Y0,  fill='yellow')
        '''

        pointxc=220
        pointyc=300
        
        
        
        '''        
        if data['umf']<=40 and data['umf']>0:
            #cumf=cvs.create_oval(495, 160, 555, 220, fill="red")#umf
            umfx,umfy,umfx1,umfy1=chan(185,150,235,150)
            lineumf = cvs.create_line(umfx, umfy, umfx1, umfy1, fill="purple",width=10)#umf
            
        if data['ulf']<=40 and data['ulf']>1 or data['lld']<=40:
            #culf=cvs.create_oval(400, 160, 460, 220, fill="red")#ulf
            ulfx,ulfy,ulfx1,ulfy1=chan(130,150,185,150)
            lineulf = cvs.create_line(ulfx, ulfy,ulfx1, ulfy1, fill="purple",width=10)#ulf

        if data['urf']<=40 and data['urf']>1 or data['rrd']<=40:
            
            #curf=cvs.create_oval(590, 160, 650, 220, fill="red")#urf
            urx,ury,ur1x,ur1y=chan(235,150,295,150)
            lineurf = cvs.create_line(urx, ury, ur1x, ur1y, fill="purple",width=10)#urf
            
            
        if data['l1d']<=130:
            l1x,l1y,l11x,l11y=chan(130,150,80,200)
            linel1d = cvs.create_line(l1x,l1y,l11x,l11y, fill="purple",width=10)#l1d
            #l1cx,l1cy,l11cx,l11cy=chan(250,160,310,220)
            #cl11d=cvs.create_oval(l1cx,l1cy,l11cx,l11cy, fill="red")#l1d
            
        if data['r1d']<=130:
            #cr1d=cvs.create_oval(690, 160, 750, 220, fill="red")#r1d
            r1dx,r1dy,r11dx,r11dy=chan(295,150,345,200)
            liner1d = cvs.create_line(r1dx, r1dy, r11dx, r11dy, fill="purple",width=10)#r1d
            
        if data['ull']<=30 and data['ull']>=1:
            ullx,ully,ull1x,ull1y=chan(80,200,80,310)
            lineull = cvs.create_line(ullx,ully,ull1x,ull1y, fill="purple",width=10)#rll
            #cull=cvs.create_oval(300, 300, 360, 360, fill="red")#ull
        if data['ul2']<=30 and data['ul2']>=1:
            ul2x,ul2y,ul21x,ul21y=chan(80,310,80,420)
            lineul2 = cvs.create_line(ul2x,ul2y,ul21x,ul21y, fill="purple",width=10)#rl2
            #cul2=cvs.create_oval(300, 440, 360, 500, fill="red")#ul2
        if data['urr']<=30 and data['urr']>=1:
            urrx,urry,urr1x,urr1y=chan(345,200,345,300)
            lineurr = cvs.create_line(urrx, urry, urr1x, urr1y, fill="purple",width=10)#urr
            #curr=cvs.create_oval(295, 150, 295, 250, fill="red")#urr
        if data['ur2']<=30 and data['ur2']>=1:
            ur2x,ur2y,ur21x,ur21y=chan(345,300,345,420)
            lineur2 = cvs.create_line(ur2x,ur2y,ur21x,ur21y, fill="purple",width=10)#ur2
            #cur2=cvs.create_oval(690, 440, 750, 500, fill="red")#ur2
                        
        if data['ubb']<=40 and data['ubb']>=1:
            #cubb=cvs.create_oval(495, 600, 555, 660, fill="red")#rbb
            ubbx,ubby,ubb1x,ubb1y=chan(80,420,345,420)
            lineubb = cvs.create_line(ubbx,ubby,ubb1x,ubb1y, fill="purple",width=10)#ubb

        '''
        
        cvs.update()
        cvs.delete(cardot)      
        car_x1=car_x2
        car_y1=car_y2
        
        
        '''
        if data['umf']<=40 and data['umf']>0:
            cvs.delete(lineumf)
        if data['ulf']<=40 and data['ulf']>1 or data['lld']<=40:
            cvs.delete(lineulf)
        if data['urf']<=40 and data['urf']>1 or data['rrd']<=40:
            cvs.delete(lineurf)
        if data['l1d']<=130:
            cvs.delete(linel1d)
        if data['r1d']<=130:
            cvs.delete(liner1d)
        if data['ull']<=30 and data['ull']>=1:
            cvs.delete(lineull)
        if data['ul2']<=30 and data['ul2']>=1:
            cvs.delete(lineul2)
        if data['urr']<=30 and data['urr']>=1:
            cvs.delete(lineurr)
        if data['ur2']<=30 and data['ur2']>=1:
            cvs.delete(lineur2)
        if data['ubb']<=40 and data['ubb']>=1:
            cvs.delete(lineubb)
        '''    
              
        #for i in range(len(data['setx'])):
           # cvs.delete(spoint[i])        
        spoint.clear()
        end=time.time()
        print("執行時間：%f 秒" % (end - start))
        '''
        while True:
         
            r=0
            client = mqtt.Client("ddg") #create new instance要記得更改，隨便一個id都可以
            datam=client.on_message=on_message #attach function to callback
            client.connect(broker_address) #connect to broker
            client.subscribe("ulcar/toby")
            client.loop_start() #start the loop
            time.sleep(0.5)
            client.loop_stop()      
            if r==5 :
                f=open('小小10000.txt','a')
                f.write(datam)
                f.write('\n')
                f.close()
                data=eval(datam)
                print(data)
                break
        '''
        
        #刪除要重繪的東西
      #刪除!!
    #data=givedataul.getdata()   
    win.mainloop()
    win.bind("<Destroy>", _destroy)        


def animate(win):
    tk.Canvas.cvs.update()
    
if __name__ == "__main__":
    #sort_data.Open()
    
    #先讀取幾次把剛開機不完整的資料讀取掉
    """
    time.sleep(0.1)
    data=sort_data.getdata()
    time.sleep(0.1)
    data=sort_data.getdata()
    time.sleep(0.1)
    data=sort_data.getdata()
    """
    
    win = tk.Tk()
    motion(win)