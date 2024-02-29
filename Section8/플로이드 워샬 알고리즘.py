import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/12. 플로이드 워샬 알고리즘/in1.txt")

n,m=map(int,input().split())
dis=[[5000]*(n+1) for _ in range(n+1)]
for i in range(n):
    dis[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    dis[a][b]=c

for t in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][t]+dis[t][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j]==5000:
            print("M",end=' ')
        else:
            print(dis[i][j],end=' ')
    print()
