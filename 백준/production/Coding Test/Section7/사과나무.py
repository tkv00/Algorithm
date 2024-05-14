from collections import deque
import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 7/8. 사과나무/in1.txt")

N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
sum=a[N//2][N//2]
ch=[[0]*N for _ in range(N)]
ch[N//2][N//2]=1
dx=[1,0,-1,0]
dy=[0,1,0,-1]
k=N//2
t=0
n=N

dQ=deque()
dQ.append([k,k])
for _ in range(N//2):
    now=dQ.popleft()
    for next in ((now[0]+dx[0],now[1]+dy[0]),(now[0]+dx[1],now[1]+dy[1]),(now[0]+dx[2],now[1]+dy[2]),(now[0]+dx[3],now[1]+dy[3])):
        if  ch[next[0]][next[1]]==0:
            dQ.append(next)
            ch[next[0]][next[1]]=1
            print(a[next[0]][next[1]])
            sum+=a[next[0]][next[1]]
print(sum)
