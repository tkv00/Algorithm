def DFS(weight,day):
    global K,N,cnt
    if weight<500:
        return
    if day==N:
        cnt+=1
        return
    else:
        for i in range(N):
            if ch[i]==0:
                ch[i]=1
                DFS(weight+a[i]-K,day+1)
                ch[i]=0


if __name__=="__main__":
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    cnt=0
    ch=[0]*N
    DFS(500,0)
    print(cnt)
    
