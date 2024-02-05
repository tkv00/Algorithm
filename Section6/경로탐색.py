import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 6/15. 경로탐색/in1.txt")

def DFS(L):
    global cnt
    
    if n==L:
        for num in path:
            print(num,end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if a[L][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0

if __name__=="__main__":
    n,m=map(int,input().split())
    a=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        k,v=map(int,input().split())
        a[k][v]=1
    ch=[0]*(n+1)
    cnt=0
    ch[1]=1
    path=[]
    path.append(1)
    DFS(1)
    print(cnt)