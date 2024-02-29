n=int(input())
a=[int(input()) for _ in range(n)]
num=[1,2,3]
dp=[0]*(max(a)+1)

dp[0]=1
for i in range(3):
    for j in range(num[i],max(a)+1):
        dp[j]+=dp[j-num[i]]
for i in range(n):
    print(dp[a[i]])
