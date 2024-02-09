
import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/9. 미로의 최단거리 통로/in5.txt")

from collections import deque
a=[list(map(int,input().split())) for _ in range(7)]
ch=[[0]*7 for _ in range(7)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
dQ=deque()
dQ.append((0,0))
ch[0][0]=0
while dQ:
    tmp=dQ.popleft()
    for i in range(4):
        x=dx[i]+tmp[0]
        y=dy[i]+tmp[1]
        if   0<=x<7 and 0<=y<7 and a[x][y]==0 and ch[x][y]==0:
            ch[x][y]+=ch[tmp[0]][tmp[1]]+1
            dQ.append((x,y))

if ch[6][6]==0:
    print(-1)
else:
    print(ch[6][6])
                
