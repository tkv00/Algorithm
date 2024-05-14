from collections import deque
def BFS(x,y):
    dq=deque()
    dq.append((x,y))
    time=1
    while dq:
        next=dq.popleft()
        for i in range(4):
            nextX=next[0]+dx[i]
            nextY=next[1]+dy[i]
            if 0<=nextX<n and 0<=nextY<m and ch[nextX][nextY]:
                a[nextX][nextY]=1

if __name__=="__main__":
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    n,m=map(int,input().split())
    a=[list(input()) for _ in range(n)]
    ch=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j]=='#' :
                ch[i][j]=1
            if a[i][j]=='F':
                ch[i][j]=1
                fireX=i
                fireY=j
    