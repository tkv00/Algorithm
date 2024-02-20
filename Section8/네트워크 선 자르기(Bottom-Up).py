import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/1, 2. 네트워크 선 자르기/in5.txt")


N=int(sys.stdin.readline())
dp=[0]*(N+1)
dp[0],dp[1]=1,2
for i in range(2,N+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N-1])