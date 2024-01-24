def DFS(v):
    if v==n+1:
        for i in range(n):
            if ch[i]==0:
                res1.append(ch[i])
            else:
                res2.append(ch[i])
    else:
        DFS(v+1)
        ch[v]=1
        DFS(v+1)
        ch[v]=0

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    res1=[]
    res2=[]
    print(res1)
    print(res2)
