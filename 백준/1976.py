def getSet(list,x):
    if list[x]==x:
        return x
    return getSet(list,list[x])

def unionSet(list,a,b):
    a=getSet(list,a)
    b=getSet(list,b)
    if a<b:
        list[b]=a
    else:
        list[a]=b

if __name__=="__main__":
    N=int(input())
    M=int(input())
    for i in range(1,N+1):
            
    plan=list(map(int,input().split()))
    ch[plan[0]]=1
    DFS(0,plan[0])
    print("NO")