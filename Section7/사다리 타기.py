import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/16. 사다리타기/in1.txt")

def DFS(L,x,y):
    global cnt
    if a[x][y]==2:
        print(cnt)
        sys.exit(0)
    else:
        if L==0:
            for i in range(10):
                cnt=i
                ch[x][y]=1
                DFS(L+1,x,y+i)
                ch[x][y]=0
        else:
            path_count=0
            next_path=-1
            
            for j in range(3):
                xx=x+dx[j]
                yy=y+dy[j]
                if 0<=xx<10 and 0<=yy<10 and a[xx][yy]==1 and ch[xx][yy]==0 :
                    next_path=j
                    path_count+=1
                    
            
            #갈 수 있는 방향이 아래로 하나만 있는 경우
            if path_count==1:
                ch[xx][yy]=1
                DFS(L+1,x+dx[next_path],y+dy[next_path])
                ch[xx][yy]=0
            #여러 방향으로 이동이 가능
            elif path_count>1:
                for k in range(3):
                    xx=x+dx[k]
                    yy=y+dy[k]
                    if 0<=xx<10 and 0<=yy<10 and a[xx][yy]==1 and ch[xx][yy]==0  :
                        ch[xx][yy]=1
                        DFS(L+1,xx,yy)
                        ch[xx][yy]=0
                        
if __name__=="__main__":
    a=[list(map(int,input().split())) for _ in range(10)]
    dy=[1,-1,0]#우 좌 히
    dx=[0,0,1]
    cnt=0
    ch=[[0]*10 for _ in range(10)]
    DFS(0,0,0)


