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
f=open("maxnet_input.txt")
line_number=0
while True:
            line=f.readline()
            line=line.rstrip('\n')
            if len(line)==0:
                break
            line_number+=1
            word=line.split('=')
            if line_number==1:
                m=int(word[1])
                y_in=y_in*m
            if line_number==3:
                x=word[1].split(',')
                for i in range(x.__len__()):
                    y_in[i]=float(x[i])
            if line_number==2:
                delta=float(word[1])
                        
f.close();    
while True:
    epoch+=1
    y_out=[]
    for i in range(0,m):    
        if y_in[i]>=0:
            y_out.append(y_in[i])
        else:
            y_out.append(0)
    if len(winner_takes_all(y_out))==1:
        print('winner unit is : ',winner_takes_all(y_out)[0]+1) 
        break
    for i in range(0,m):
        y_in[i]=y_out[i]-(sum(y_out)-y_out[i])*delta
    if epoch==100:
        break
