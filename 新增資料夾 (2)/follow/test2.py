
f= open('test.txt','r ') 
while True:
    
    s=f.read(1)
    print(s)
    if s=='a':
        f.write('999')
    if s=='Z':
        break

            
