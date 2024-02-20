import sys
N=int(sys.stdin.readline())
score=[0]*(N+1)
for i in range(1,N+1):
    score[i]=int(sys.stdin.readline())
dp=[0]*(N+1)
dp[1],dp[2]=score[1],score[1]+score[2]

for i in range(3,N+1):
    dp[i]=max(score[i]+score[i-1]+dp[i-3],score[i]+dp[i-2])
print(dp[-1])
