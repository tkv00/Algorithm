import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/12. 단지번호붙이기/in5.txt")

from collections import deque
def find_max(a):
    max=-214700000
    for i in range(len(a)):
        for j in range(len(a)):
            if max<a[i][j]:
                max=a[i][j]
    return max-1

def BFS(a,x,y):
    global cnt
    res=0
    dq=deque()
    dq.append((x,y))
    while dq:
        pt=dq.popleft()
        for i in range(4):
            xx=dx[i]+pt[0]
            yy=dy[i]+pt[1]
            if 0<=xx<N and 0<=yy<N and a[xx][yy]==1:
                dq.append((xx,yy))
                a[xx][yy]=cnt
                res+=1
    cnt+=1
    return res
    
N=int(input())
a=[list(map(int,input())) for _ in range(N)]
cnt=2
res_cnt=[]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(N):
    for j in range(N):
        if a[i][j]==1:
            res_cnt.append(BFS(a,i,j))
print(len(res_cnt))
res_cnt.sort()
for num in res_cnt:
    if num==0:
        num=1
    print(num)
