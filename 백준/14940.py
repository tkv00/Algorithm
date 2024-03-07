from collections import deque
def BFS(x,y):
    global end_x,end_y
    dq=deque()
    dq.append((x,y))
    while dq:
        point=dq.popleft()
        for i in range(4):
            xx=point[0]+dx[i]
            yy=point[1]+dy[i]
            if 0<=xx<N and 0<=yy<M and res[xx][yy]==0 and a[xx][yy]==1:
                res[xx][yy]=res[point[0]][point[1]]+1
                dq.append((xx,yy))

    
if __name__=="__main__":
    N,M=map(int,input().split())
    #N은 행의 크기,M은 열의 크기
    a=[list(map(int,input().split())) for _ in range(N)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    res=[[0]*(M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if a[i][j]==2:
                BFS(i,j)
    for i in range(N):
        for j in range(M):
            if a[i][j]==1 and res[i][j]==0:
                res[i][j]=-1
    for i in range(N):
        for j in range(M):
            print(res[i][j],end=' ')
        print()
    