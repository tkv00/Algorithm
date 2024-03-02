from collections import deque

def BFS(x,y):
    global cnt
    a[x][y]=1
    V=1
    dq=deque()
    dq.append((x,y))
    while dq:
        pt=dq.popleft()
        for i in range(4):
            xx=dx[i]+pt[0]
            yy=dy[i]+pt[1]
            if 0<=xx<N and 0<=yy<M and a[xx][yy]==0:
                dq.append((xx,yy))
                a[xx][yy]=1
                V+=1
    result.append(V)
    cnt+=1

M,N,K=map(int,input().split())
a=[[0]*(M) for _ in range(N)]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            a[j][k]=1
result=[]
cnt=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for i in range(N):
    for j in range(M):
        if a[i][j]==0:
            BFS(i,j)
print(cnt)
result.sort()
for x in result:
    print(x,end=' ')
