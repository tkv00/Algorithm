def DFS(L):
    if L==m:
        for num in res:
            print(num,end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                
        




if __name__=="__main__":
    n,m=map(int,input().split())
    ch=[0]*(n+1)
    res=[0]*m
    cnt=0