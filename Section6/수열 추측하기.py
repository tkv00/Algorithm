def DFS(L):
    if L+1==n:
        for num in res:
            print(num,end=' ')
    else:
        for i in range(1,n+1):
            DFS(L+1)





if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*n
    DFS(0)