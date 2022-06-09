from PID import PID
pid=PID(p=2,i=0.5,d=0.01,imax=10)
error=[30,50,55,10,50,80,40,60,-50,10]
print(len(error))
for i in range(9):
    output=pid.get_pid(error[i],1)
    print(output)