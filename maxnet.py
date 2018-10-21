def winner(mylist):  
    a=[]
    for i in range(0,len(mylist)):
        if mylist[i]>0:
            a.append(i)
    return a
    
m=0     
delta=0
yin=[0] 
epoch=0    
f=open("maxnet_input.txt")
linenumber=0
while True:
            line=f.readline()
            line=line.rstrip('\n')
            if len(line)==0:
                break
            linenumber+=1
            word=line.split('=')
            if linenumber==1:
                m=int(word[1])
                yin=yin*m
            if linenumber==3:
                x=word[1].split(',')
                for i in range(x.__len__()):
                    yin[i]=float(x[i])
            if linenumber==2:
                delta=float(word[1])
                        
f.close();    
while True:
    epoch+=1
    yout=[]
    for i in range(0,m):    
        if yin[i]>=0:
            yout.append(yin[i])
        else:
            yout.append(0)
    if len(winner(yout))==1:
        print('winner unit is : ',winner(yout)[0]+1) 
        break
    for i in range(0,m):
        yin[i]=yout[i]-(sum(yout)-yout[i])*delta
    if epoch==100:
        break
