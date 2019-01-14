import numpy as np
input=[.05,.10]
target=[.01,.99]
hiden=[]
weight=[]
biase=[.35,.60,.65]
#############################
def network(input,output,noofhiden=1,nodeinhiden=2):
    wt=[]
    for i in range(noofhiden):
        if(i<1):
            weight=np.random.rand(nodeinhiden,len(input))
        else:
            weight=np,random.rand(nodeinhiden,nodeinhiden)
        wt.append(weight)
        outlayer=np.random.rand(output,nodeinhiden)
        wt.append(outlayer)

    return (wt)
###############################
def feedforword(input,w ,biase):
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
    return(h)
###############################
def sigmoid(x):
    a=[]
    for i in x:
        b=1/(1+np.exp(-i))
        a.append(b)
    return(a)
#################################
def update(wt,err,eta=.5):
    return(wt-eta*err)
################################
def error(output,target,outh):
    etWo=output-target
    oWn=output*(1-output)
    nWw=outh
    return(etWo*oWn*nWw)
#################################
w=network(input,2)
neth=[]
outh=[]
for k in range(len(w)):
    net=feedforword(input,w[k],biase[k])
    print("net"+str(net))
    out=sigmoid(net)
    neth.append(net)
    outh.append(out)
    input=out
print(neth)
print(outh)
