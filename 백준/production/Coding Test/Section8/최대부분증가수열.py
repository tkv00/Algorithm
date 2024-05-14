import sys
sys.stdin=open("/Users/kimdoyeon/Desktop/pythonalgorithm_formac/섹션 8/4. 최대부분증가수열/in2.txt")
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
dp=[0]*(n+1)
dp[1]=1
res=0
max_num=dp[1]
for i in range(2,n+1):
    max=0
    for j in range(1,i):
        if a[j]<a[i] and dp[j]>max:
            max=dp[j]
    dp[i]=max+1
    if res<dp[i]:
        res=dp[i]
print(res)