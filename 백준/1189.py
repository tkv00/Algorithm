from collections import deque
def DFS(x,y,length):
    global res,K
    if length>K:
        return
    if x==0 and y==C-1 and length==K:
        res+=1
        return
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<R and 0<=yy<C and check[xx][yy]==0 and a[xx][yy]!='T' :
                check[xx][yy]=1
                DFS(xx,yy,length+1)
                check[xx][yy]=0


if __name__=="__main__":
    R,C,K=map(int,input().split())
    a=[]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    res=0
    check=[[0]*C for _ in range(R)]
    for i in range(R):
        a.append(list(input()))
    check[R-1][0]=1
    DFS(R-1,0,1)
    print(res)