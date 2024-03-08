import math
N,D=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
dp=[0]*(D+1)
for i in range(D+1):
    dp[i]=i
for i in range(D+1):
    if i>0:
        dp[i]=min(dp[i],dp[i-1]+1)
    for start,end,length in a:
        if end<=D and i==start:
            dp[end]=min(dp[end],dp[start]+length)
print(dp[D])