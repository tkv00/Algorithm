import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/11. 등산경로/in5.txt")

def DFS(L,x,y):
    global cnt
    global end
    global start
    if x==end_xy[0] and y==end_xy[1]:
        cnt+=1
    else:
        if 0<=x<N and 0<=y<N and ch[x][y]==0:
            for i in range(4):
                xx=dx[i]
                yy=dy[i]
                if 0<=x+xx<N and 0<=y+yy<N and a[x][y]<a[x+xx][y+yy]:
                    ch[x][y]=1
                    DFS(L+1,x+xx,y+yy)
                    ch[x][y]=0
    

if __name__=="__main__":
    N=int(input())
    a=[list(map(int,input().split())) for _ in range(N)]
    end=-2147000000
    start=2147000000
    start_xy=[0]*2
    end_xy=[0]*2
    for i in range(N):
        for j in range(N):
            if start>a[i][j]:
                start=a[i][j]
                start_xy[0]=i
                start_xy[1]=j
            if end<a[i][j]:
                end=a[i][j]
                end_xy[0]=i
                end_xy[1]=j
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    cnt=0
    ch=[[0]*N for _ in range(N)]
    DFS(0,start_xy[0],start_xy[1])
    print(cnt)