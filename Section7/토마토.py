import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/15. 토마토/in1.txt")
from collections import deque
#보드판에 0이 없어야함
def is_board(a):
    for i in range(M):
        for j in range(N):
            if a[i][j]==0:
                return False
    return True
def BFS(a):
    cnt=0
    dq=deque(res)
    while dq:
        for _ in range(len(dq)):  # 그 날 처리할 토마토의 수만큼 반복
            x, y = dq.popleft()
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < M and 0 <= yy < N and a[xx][yy] == 0:
                    a[xx][yy] = 1
                    dq.append((xx, yy))
        if dq:  # 변화가 있었으면 일수 증가
            cnt += 1
    return cnt

N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(M)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]
res=[]
for i in range(M):
    for j in range(N):
        if a[i][j]==1:
            res.append((i,j))
k=BFS(a)

if is_board(a):
    print(k)
else:
    print(-1)
