n,money=map(int,input().split())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)
dp=[0]*(money+1)
dp[0]=1
for i in range(n):
    for j in range(a[i],money+1):
        dp[j]=dp[j]+dp[j-a[i]]

print(dp[money])