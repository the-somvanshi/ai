import numpy as np
import copy

######################################
def network(input,output,nofhiden=2,nodeinhiden=2):
    global biase
    wt=[]
    biase=np.random.rand(nofhiden+1)
    for i in range(nofhiden):
        if(i<1):
            weight=np.random.rand(nodeinhiden,len(input))
        else:
            weight=np.random.rand(nodeinhiden,nodeinhiden)
        wt.append(weight)
    outlayer=np.random.rand(output,nodeinhiden)
    wt.append(outlayer)           
##    we=[[1,2],[3,4]]
##    wc=[[5,6],[7,8]]
##    wt.append(we)
##    wt.append(wc)
    return (wt)
######################################

def feedforword(input,w,biase):
    s=(np.matrix(w)).size
    out=s/len(input)
    h=[]
    for i in range(int(out)):
        a=0
        for j in range(len(input)):
            a+=w[i][j]*input[j]
        h.append(a)
    for i in range(len(h)):
       h[i]=h[i]+biase   
    return (h)
    
######################################
def sigmoid(x):
    a=[]
    for i in x:
        b=1/(1+np.exp(-i))
        a.append(b)
    return a
######################################
def errwt(alpha,out):
    alpha.reverse()
    out.insert(0,input)
    cw=[]
    out.pop()
    for i in range(len(out)):
        e=np.matrix(alpha.pop()).transpose()*out.pop()
        cw.append(e)
    return cw
#####################################
def err1(input,output,target,w):
    wt=w
    wz=w
    tz=target
    print(len(wz))
    out=output
    z=[]
    alpha=[]
    salpha=[]
    for i in range(len(target)):
        dif=output[len(output)-1][i]-target[i]
        der=output[len(output)-1][i]*(1-output[len(output)-1][i])
        mul=dif*der
        alpha.insert(0,mul)
        z.append(mul)
    salpha.append(z)
    o=out.pop()
    o=out.pop()
    for i in range(len(w)-1):
        temp=[]
        s=np.matrix(alpha)*np.matrix(wt.pop())
        for i in range(len(s)):
            b=s[i]*o[i]*(1-o[i])
            temp.append(b)
            salpha.append(np.array(b))
        temp=np.array(temp).reshape(s.size,)
        alpha.clear()
        alpha.append(temp)
    return salpha
#####################################
def update(wt,err,eta=.5):
    print(err)
    a=[]
    for x in err:
        z=x*eta
        a.append(z)
    #print(a)
    d=np.subtract(wt,a)
   # print(d)
    return(d)
 #######################################
def bp(input):
    for k in range(len(w)):
        net=feedforword(input,w[k],biase[k])
        out=sigmoid(net)
        neth.append(net)
        outh.append(out)
        input=out
#####################################
input=[2,2]
target=[4,1]
hiden=[]
weight=[]
biase=[]
neth=[]
outh=[]
w=network(input,len(target))
print("weight"+str(w))
bp(input)
nout=copy.deepcopy(outh)
gw=copy.deepcopy(w)
e=err1(input,nout,target,gw)
z=errwt(e,outh)
nw=update(w,z)
print(nw)
w=nw

