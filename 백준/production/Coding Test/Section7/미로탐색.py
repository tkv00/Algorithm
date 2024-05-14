import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/10. 미로탐색/in5.txt")

def DFS(L,x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
        
    else:
        for i in range(4):
            if 0<=x<7 and 0<=y<7 and ch[x][y]==0 and a[x][y]==0:
                ch[x][y]=1
                DFS(L+1,x+dx[i],y+dy[i])
                ch[x][y]=0



if __name__=="__main__":
    cnt=0
    a=[list(map(int,input().split())) for _ in range(7)]
    ch=[[0]*7 for _ in range(7)]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    DFS(0,0,0)
    print(cnt)
