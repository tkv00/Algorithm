import sys
INF=sys.maxsize
#sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/13. 회장뽑기/in1.txt")

n=int(input())
friend=[[INF]*(n+1) for _ in range(n+1)]

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    else:
        friend[a][b]=1
        friend[b][a]=1
for i in range(1,n+1):
    friend[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            friend[i][j]=min(friend[i][j],friend[i][k]+friend[k][j])
res=[0]*(n+1)
score=1000
for i in range(1,n+1):
    for j in range(1,n+1):
        res[i]=max(res[i],friend[i][j])
    score=min(score,res[i])
out=[]
for i in range(1,n+1):
    if res[i]==score:
        out.append(i)
print("%d %d"%(score,len(out)))
for x in out:
    print(x,end=' ')
