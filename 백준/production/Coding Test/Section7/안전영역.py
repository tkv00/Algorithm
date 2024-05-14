import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/14. 안전영역/in5.txt")

from collections import deque
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
def BFS(x,y,k):
    global cnt
    dq=deque()
    dq.append((x,y))
    while dq:
        res=dq.popleft()
        for i in range(4):
            xx=res[0]+dx[i]
            yy=res[1]+dy[i]
            if 0<=xx<N and 0<=yy<N and  a[xx][yy]>k and ch[xx][yy]==0:
                dq.append((xx,yy))
                ch[xx][yy]=1
dx=[1,0,-1,0]
dy=[0,1,0,-1]
max_num=-214700000
for i in range(N):
    for j in range(N):
        if max_num<a[i][j]:
            max_num=a[i][j]
res=0
for k in range(max_num+1):
    cnt=0
    ch=[[0]*N for _ in range(N)]
    for i in range (N):
        for j in range(N):
            if k<a[i][j] and ch[i][j]==0:
                ch[i][j]=1
                BFS(i,j,k)
                cnt+=1
    res=max(cnt,res)
print(res)


