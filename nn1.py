import numpy as np
input=[.05]
target=[1]
hiden=[]
weight=[]
biase=[0.35,.60,0.65,1,5,6]
######################################
def network(input,output,nofhiden=1,nodeinhiden=1):
    wt=[]
    for i in range(nofhiden):
        if(i<1):
            weight=np.random.rand(nodeinhiden,len(input))
        else:
            weight=np.random.rand(nodeinhiden,nodeinhiden)
        wt.append(weight)
    outlayer=np.random.rand(output,nodeinhiden)
    wt.append(outlayer)           
##    we=[[.15,.20],[.25,.30]]
##    wc=[[.40,.45],[.50,.55]]
##    wt.append(we)
    #wt.append(wt)
    
    return (wt)
######################################

def feedforword(input,w,biase):
    #print(w)
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
#####################################
def error(output,target,outh):
    #$etotal/output----output is last node of output--etotal is total error of network
    etWo=output-target
    print("diff"+str((etWo/target)*100)+"%")
    #$output/$net-----net is without sigmoid value---output is sigmoid value
    oWn=output*(1-output)
    #$net/$wieght-----weight is weight that come to node for which we are calculating error
    nWw=outh
    #etotal/weight
    return (etWo*oWn*nWw)
#####################################
def update(wt,err,eta=.5):
    return(wt-eta*err)
#######################################
w=network(input,len(target))
print("weight"+str(w))
neth=[]
outh=[]
def bp(input):
    for k in range(len(w)):
        net=feedforword(input,w[k],biase[k])
       # print("net"+str(net))
        out=sigmoid(net)
       # print("out"+str(out))
        neth.append(net)
        outh.append(out)
        input=out
   # print("neth"+str(neth))
    print("out"+str(outh))
    dic()
def dic():    
    e=error(outh[1][0],target[0],outh[0][0])
    w[1][0]=update(w[1][0],e)
    print(w)
for i in range(20):
    bp(input)
    
        
