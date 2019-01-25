import numpy as np
input=[2,2,7,4,5,7,5,8]
target=[4,1,3]
hiden=[]
weight=[]
biase=[]
######################################
def network(input,output,nofhiden=2,nodeinhiden=4):
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
######################################
def errwt(alpha,out):
    cw=[]
    e=alpha.pop()*out.pop()
    cw.append(e)
    return cw
#####################################
def err1(input,output,target,w):
    wt=w
    out=output
    z=[]
    alpha=[]
    salpha=[]
    for i in range(len(target)):
        dif=output[len(output)-1][i]-target[i]
        der=output[len(output)-1][i]*(1-output[len(output)-1][i])
        z=alpha.insert(0,dif*der)
        salpha.append(dif*der)
    print("alpha isz"+str(alpha))
    out.insert(0,input)
    o=out.pop()
    o=out.pop()
    for i in range(len(w)-1):
        temp=[]
        print("alpha in loop"+str(alpha)+"shape"+str(np.array(alpha).shape))
        s=np.matrix(alpha)*np.matrix(wt.pop())
        print("s"+str(s))
        for i in range(len(s)):
            b=s[i]*o[i]*(1-o[i])
            temp.append(b)
            salpha.append(np.array(b))
            print("@"+str(b))
        alpha.clear()
        print("weight1 isz"+str(temp))
        temp=np.array(temp).reshape(4,)
        alpha.append(temp)
        print("new alpha"+str(alpha))
        
    return salpha

    
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
print("biasae"+str(biase))
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
   # print("out"+str(outh))

bp(input)
e=err1(input,outh,target,w)
#z=errwt(e,outh)
#print("sende"+str(z))
print(len(e))
