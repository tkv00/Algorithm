import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/10. 동전교환/in5.txt")

n=int(input())
a=list(map(int,input().split()))
money=int(input())
dp=[0]*(money+1)

for i in range(n):
    for j in range(a[i],money+1):
        if dp[j]!=0:
            dp[j]=min(dp[j],dp[j-a[i]]+1)
        else:
            dp[j]=j//a[i]
print(dp[money])