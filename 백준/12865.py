N,K=map(int,input().split())
a=[]
a.append((0,0))
for i in range(N):
    W,V=map(int,input().split())
    a.append((W,V))
dp=[[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        w=a[i][0]
        if w>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+a[i][1])
print(dp[N][K])