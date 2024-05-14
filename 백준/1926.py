from collections import deque
def BFS(x,y):
    a[x][y]=0
    cnt=1
    dq=deque()
    dq.append((x,y))
    while dq:
        k=dq.popleft()
        for i in range(4):
            nextX=k[0]+dx[i]
            nextY=k[1]+dy[i]
            if 0<=nextX<n and 0<=nextY<m and a[nextX][nextY]==1:
                a[nextX][nextY]=0
                cnt+=1
                dq.append((nextX,nextY))
    return cnt
if __name__=="__main__":
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    n,m=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(n)]
    res=0
    res2=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                res2=max(BFS(i,j),res2)
                res+=1
    print(res)
    print(res2)