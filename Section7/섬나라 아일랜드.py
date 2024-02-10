import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/13. 섬나라 아일랜드/in4.txt")
from collections import deque
# 입략받은 배열중 바다인 부분은 1로 선언
#값이 1인 아닌 곳에서부터 BFS탐색 후 deque가 비면 cnt하나 추가
#입략 받은 배열의 값이 모두 1이 될 때까지 반복
#이 때, 혼자있는 섬은 카운트 하지않는다.

def BFS(a,x,y):
    res=0
    dq=deque()
    dq.append((x,y))#시작점
    while dq:
        point=dq.popleft()
        for i in range(8):
            xx=point[0]+dx[i]
            yy=point[1]+dy[i]
            if 0<=xx<N and 0<=yy<N and a[xx][yy]==1:
                res+=1
                a[xx][yy]=0
                dq.append((xx,yy))
    

N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]

cnt=0
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,1,-1,1,-1]

for i in range(N):
    for j in range(N):
        if a[i][j]==1:
            BFS(a,i,j)
            cnt+=1

print(cnt)




