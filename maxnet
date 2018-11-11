def winner_takes_all(my_list):  
    array=[]
    for i in range(0,len(my_list)):
        if my_list[i]>0:
            array.append(i)
    return array
m=0     
delta=0
y_in=[0] 
epoch=0    
m=int(input("enter no of node "))
delta=float(input("enter delta"))
y_in=y_in*m
for i in range(m):
    e=float(input("enter initial value"))
    y_in[i]=e
    
while True:
    epoch+=1
    y_out=[]
    for i in range(0,m):    
        if y_in[i]>=0:
            y_out.append(y_in[i])
        else:
            y_out.append(0)
    if len(winner_takes_all(y_out))==1:
        print('winner is unit : ',winner_takes_all(y_out)[0]+1) 
        break
    for i in range(0,m):
        y_in[i]=y_out[i]-(sum(y_out)-y_out[i])*delta
        
    if epoch==100:
        break
print(epoch)        
