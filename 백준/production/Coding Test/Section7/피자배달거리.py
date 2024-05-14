
import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/17. 피자 배달 거리/in1.txt")
def DFS(L,s):

    if L==M:
        dis=2147000000
        cnt=0
        for i in range(len(house)):
            x1=house[i][0]
            y1=house[i][1]
            for j in con:
                x2=pz[j][0]
                y2=pz[j][1]
                dis= min(dis,abs(x1-x2)+abs(y1-y2))
            cnt+=dis
        if dis<cnt:
            cnt=dis

    else:
        for i in range(s,len(pz)):
            con[L]=i
            DFS(L+1,i+1)

if __name__=="__main__":
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]
    pz=[]
    house=[]
    con=[0]*M
    for i in range(N):
        for j in range(N):
            if a[i][j]==2:
                pz.append((i,j))
            if a[i][j]==1:
                house.append((i,j))
    DFS(0,0)
